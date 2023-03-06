import PyPDF2

# Take user input for the PDF filename
pdf_file = input("Enter the filename of the PDF to print: ")

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(open(pdf_file, 'rb'))

# Take user input for the number of pages to print
num_pages = int(input("Enter the number of pages to print: "))

# Take user input for the paper orientation
orientation = input("Enter the paper orientation (portrait or landscape): ")

# Take user input for color/grayscale printing
color_mode = input("Enter the printing color mode (color or grayscale): ")

# Take user input for paper size
paper_size = input("Enter the paper size (A4, Letter, etc.): ")

# Create a PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Loop through the selected number of pages and add them to the PDF writer object
for page_num in range(num_pages):
    pdf_writer.add_page(pdf_reader.pages[page_num])
    page = (pdf_reader.pages[page_num])
    page.setPageDimensions(595, 842) # A4 paper size in points (1 point = 1/72 inch)

# # Set the paper orientation and size
# if orientation == 'portrait':
#     page_width = PyPDF2.inch * 8.5
#     page_height = PyPDF2.inch * 11
# else:
#     page_width = PyPDF2.inch * 11
#     page_height = PyPDF2.inch * 8.5

# # Set the paper color mode
# if color_mode == 'color':
#     color = True
# else:
#     color = False

# # Set the paper size
# if paper_size == 'A4':
#     paper_size = (PyPDF2.units.mm * 210, PyPDF2.units.mm * 297)
# elif paper_size == 'Letter':
#     paper_size = (PyPDF2.units.inch * 8.5, PyPDF2.units.inch * 11)
# else:
#     print("Invalid paper size specified.")
#     exit()

color = True
# Create a PDF print options object
pdf_print_options = PyPDF2.pdf.PrintOptions(pages=(0, num_pages-1), duplex=None, color=color, page_size=paper_size)

# Create a PDF printer object
pdf_printer = PyPDF2.pdf.Printer()

# Print the PDF with the specified print options
pdf_printer.print_file(pdf_file, print_options=pdf_print_options)
