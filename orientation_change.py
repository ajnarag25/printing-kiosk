from docx import Document
from docx.enum.section import WD_ORIENT

doc = Document('new_muscles.docx')
sections = doc.sections

for section in sections:
    if section.orientation == WD_ORIENT.PORTRAIT:
        section.orientation = WD_ORIENT.LANDSCAPE
        new_width, new_height = section.page_height, section.page_width
        section.page_width = new_width
        section.page_height = new_height
doc.save('output_documentzxc.docx')
