import io
from wand.image import Image

# Open the input PDF file
with open('outt.pdf', 'rb') as file:
    # Create a wand image object for each page of the PDF
    with Image(file=file, resolution=300) as pdf:
        # Loop through each page of the PDF
        for page in pdf.sequence:
            # Convert the page to grayscale
            with Image(page) as grayscale_page:
                grayscale_page.type = 'grayscale'
                grayscale_page.depth = 8
                # Save the grayscale page
                img_bytes = grayscale_page.make_blob('jpeg')
                # You can save or further process the grayscale image here
                # ...
         
        # You can also save the modified PDF file here
        pdf.save(filename='output_file.pdf')
