import docx

archivo = "documento.docx"
documento = docx.Document(archivo)

contenido = []
for paragrafo in documento.paragraphs:
    contenido.append(paragrafo.text)

print("\n".join(contenido))
