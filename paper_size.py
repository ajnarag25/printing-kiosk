from pypdf.generic import RectangleObject
page.cropbox = RectangleObject((0, 0, A4_w, A4_h))
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize
from pypdf.generic import RectangleObject

reader = PdfReader("input.pdf")
page = reader.pages[0]
writer = PdfWriter()

A4_w = PaperSize.A4.width
A4_h = PaperSize.A4.height

# resize page to fit inside A4
h = float(page.mediabox.height)
w = float(page.mediabox.width)
scale_factor = min(A4_h/h, A4_w/w)

transform = Transformation().scale(scale_factor,scale_factor).translate(0, A4_h/3)
page.add_transformation(transform)

page.cropbox = RectangleObject((0, 0, A4_w, A4_h))

# merge the pages to fit inside A4

# prepare A4 blank page
page_A4 = PageObject.create_blank_page(width = A4_w, height = A4_h)
page.mediabox = page_A4.mediabox
page_A4.merge_page(page)

writer.add_page(page_A4)
writer.write('output.pdf')