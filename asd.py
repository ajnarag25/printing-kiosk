# Importing the parse() function
from pdf2docx import parse

# Specifying the pdf & docx files
pdf_file = 'C:/Users/admin/Downloads/COLORED_PAGE.pdf'
docx_file = 'new_muscles.docx'

try:
    # Converting PDF to Docx
    parse(pdf_file, docx_file)
    
except:
    print('Conversion Failed')
    
else:
    print('File Converted Successfully')