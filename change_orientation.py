# import PyPDF2

# pdf_in = open('C:/Users/admin/Downloads/COLORED_PAGE.pdf', 'rb')
# pdf_reader = PyPDF2.PdfReader(pdf_in)
# pdf_writer = PyPDF2.PdfWriter()

# numofpages = pdf_reader.pages
# print(numofpages)
# numrotated = 0 
# for pagenum in range([numofpages]):
#     page = pdf_reader.getPage(pagenum)
#     mb = page.mediaBox
#     if (mb.upperRight[0] > mb.upperRight[1]) and (page.get('/Rotate') is None):
#         page.rotateCounterClockwise(90)
#         numrotated = numrotated + 1
#     pdf_writer.addPage(page)

# print(str(numrotated) + " of " + str(numofpages) + " pages were rotated")
# pdf_out = open('test_rotated.pdf', 'wb')
# pdf_writer.write(pdf_out)
# pdf_out.close()

# pdf_in.close()

import PyPDF2

# Open the PDF file in read-binary mode
with open('C:/Users/admin/Downloads/COLORED_PAGE.pdf', 'rb') as file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through each page of the input PDF file
    for page_num in range(len(pdf_reader.pages)):
        # Get the current page
        page = pdf_reader.pages[page_num]
         # Get the current media box of the page
        media_box = page.mediabox
        # Rotate the page by 90 degrees clockwise
        page.rotate(90)

        


        # Add the rotated page to the output PDF file
        pdf_writer.add_page(page)


    # Save the output PDF file
    with open('output_file.pdf', 'wb') as output:
        pdf_writer.write(output)