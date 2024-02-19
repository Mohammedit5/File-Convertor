# File Conversion App - made with Django
A file conversion app with following features - 

 - JPG to PDF conversion.
 - PDF to JPG conversion.

 - PDF to DOC
 - DOC to PDF

## Installation instructions
Open terminal and install required dependencies using following command -

    pip install -r requirements.txt

Install poppler (required for JPG to PDF)

 - Download Poppler from [this](http://blog.alivate.com.au/poppler-windows/) page.
 - Navigate to it's installation directory and add 'bin' folder to system PATH.
 - Done!

Open terminal in directory where **manage** python file resides. And then execute following command -

    python manage.py runserver
    
Go to browser and hit following url -

    localhost:8000
