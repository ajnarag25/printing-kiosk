import subprocess

def command_print(event = None):
    command = "{} {}".format('C:/xampp/htdocs/printing_kiosk/printing_kiosk/PDFtoPrinter.exe',"""C:/Users/admin/Downloads/COLORED_PAGE.pdf Brother-DCP-T500W-Printer copies=2""")
    subprocess.call(command,shell=True)

command_print()