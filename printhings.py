import win32ui
import win32print
import win32con

GHOSTSCRIPT_PATH = "C:/Users/admin/Desktop/gs/bin/gswin32.exe"
GSPRINT_PATH = "C:/Users/admin/Desktop/gs/gsprint.exe"

# YOU CAN PUT HERE THE NAME OF YOUR SPECIFIC PRINTER INSTEAD OF DEFAULT
currentprinter = win32print.GetDefaultPrinter()

win32api.ShellExecute(0, 'open', GSPRINT_PATH, '-ghostscript "'+GHOSTSCRIPT_PATH+'" -printer "'+currentprinter+'" "PDFFile.pdf"', '.', 0)