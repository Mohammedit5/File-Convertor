from django.http import HttpResponse
from django.shortcuts import render, redirect
import img2pdf
from pdf2docx import Converter

import pandas as pd
import string
import random
import os
from pdf2image import convert_from_path, convert_from_bytes
from zipfile import ZipFile
import re
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    return render(request, 'index.html')


def pdf_view(request):
    with open('./convertor/sample_10.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
        return response


def jpgToPdf(request):
    # img2pdf pip

    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/jpg2pdf', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        files_list = []
        for file in files.getlist('files'):
            files_list.append(file)

        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(path_to_upload + "/sample.pdf", "wb") as f:
            f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
        os.rename(path_to_upload + "/sample.pdf", path_to_upload + "/sample.txt")
        return render(request, 'jpgtopdf.html', {'url': str(res)})
    return render(request, 'jpgtopdf.html')


def pdftojpg(request):
    # pdf2image

    if request.method == "POST":
        # creating random folder name for each user
        res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        path_to_upload = os.path.join('./convertor/static/uploaded_files/pdf2jpg', str(res))
        os.makedirs(path_to_upload)
        files = request.FILES
        for file in files.getlist('files'):
            with open(path_to_upload + '/sample.pdf', 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)

        images = convert_from_path(path_to_upload + '/sample.pdf', 500)

        zipObj = ZipFile(path_to_upload + '/sample.zip', 'w')

        for image in images:
            image.save("/page%d.jpg" % (images.index(image)), "JPEG")
            zipObj.write("/page%d.jpg" % (images.index(image)))
            os.remove("/page%d.jpg" % (images.index(image)))

        zipObj.close()
        os.remove(path_to_upload + "/sample.pdf")
        os.rename(path_to_upload + "/sample.zip", path_to_upload + "/sample.txt")
        return render(request, 'pdftojpg.html', {'url': str(res)})
    return render(request, 'pdftojpg.html')



def pdftableextract(request):




    if request.method == "POST":
        # res = ''.join(random.choice(string.ascii_lowercase) for x in range(10))
        # path_to_upload = os.path.join('./convertor/static/uploaded_files/pdftodocx', str(res))
        # path_to_sample = os.path.join('./convertor/static/uploaded_files/sample.docx')
        # os.makedirs(path_to_upload)
        file = request.FILES['file']
        # myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        print(filename)
        path_to_upload = os.path.join('./convertor/uploaded_files/pdftodocx', filename)
        os.makedirs(path_to_upload)

        # path = default_storage.save('download.pdf', ContentFile(file.read()))
        # with open(file, "wb+") as destination:
        #     for chunk in file.chunks():
        #         destination.write(chunk)
        # print(files)
        cv = Converter('uploaded_files/'+filename)
        cv.convert(path_to_upload)      # all pages by default
        cv.close()
        return render(request, 'pdftodocx.html', {'url': str(uploaded_file_url)})
        # user file files 
    return render(request, 'pdftodocx.html')
    # pdf_file = '/convertor/uploaded_files/sample.pdf'
    # docx_file = 'path/to/sample.docx'
    # # convert pdf to docx
    # cv = Converter(files)
    # cv.convert(docx_file)      # all pages by default
    # cv.close()
  



