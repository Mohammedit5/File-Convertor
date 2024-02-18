from pdf2docx import Converter

if __name__ == '__main__':
    pdf_file = 'sample.pdf'

    word_file = 'sd.docx'

    cv = Converter(pdf_file)

    cv.convert(word_file)

    cv.close()

