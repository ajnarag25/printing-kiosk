from os.path import join
from tempfile import TemporaryDirectory
from pdf2image import convert_from_path # https://pypi.org/project/pdf2image/
from img2pdf import convert # https://pypi.org/project/img2pdf/

with TemporaryDirectory() as temp_dir: # Saves images temporarily in disk rather than RAM to speed up parsing
    # Converting pages to images
    print("Parsing pages to grayscale images. This may take a while")
    images = convert_from_path(
        "C:/Users/admin/Downloads/COLORED_PAGE.pdf",
        output_folder=temp_dir,
        grayscale=True,
        fmt="jpeg",
        thread_count=4
    )

    image_list = list()
    for page_number in range(1, len(images) + 1):
        path = join(temp_dir, "page_" + str(page_number) + ".jpeg")
        image_list.append(path)
        images[page_number-1].save(path, "JPEG") # (page_number - 1) because index starts from 0

    with open("Gray_PDF.pdf", "bw") as gray_pdf:
        gray_pdf.write(convert(image_list))

    print("The new page is saved as Gray_PDF.pdf in the current directory.")