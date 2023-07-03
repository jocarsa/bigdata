from PyPDF2 import PdfReader


with open('documento.pdf', 'rb') as file:
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    for page_number in range(num_pages):
        page = reader.pages[page_number]
        text = page.extract_text()
        print(f"Page {page_number + 1}:\n{text}\n")
