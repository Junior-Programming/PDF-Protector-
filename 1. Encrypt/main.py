from PyPDF2 import PdfReader, PdfWriter
import getpass

reader = PdfReader(
    "D:/Materi pembelajaran individu/Programing/Project Python/4. Password Protect PDF/1. Encrypt/test.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

passw = getpass.getpass(prompt="Enter Password: ")

# Add a password to the new PDF
writer.encrypt(passw)

# Save the new PDF to a file
with open("D:/Materi pembelajaran individu/Programing/Project Python/4. Password Protect PDF/1. Encrypt/encrypted-pdf.pdf", "wb") as f:
    writer.write(f)
