import PyPDF2
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 

images = convert_from_path('.pdf')
pdf_writer = PyPDF2.PdfFileWriter()
for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))
# export the searchable PDF to searchable.pdf
with open("searchable.pdf", "wb") as f:
    pdf_writer.write(f)