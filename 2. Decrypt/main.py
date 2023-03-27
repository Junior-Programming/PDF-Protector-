from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader(
    "D:/Materi pembelajaran individu/Programing/Project Python/4. Password Protect PDF/2. Decrypt/encrypted-pdf.pdf")
writer = PdfWriter()

if reader.is_encrypted:
    reader.decrypt("kali")

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Save the new PDF to a file
with open("D:/Materi pembelajaran individu/Programing/Project Python/4. Password Protect PDF/2. Decrypt/decrypted-pdf.pdf", "wb") as f:
    writer.write(f)
