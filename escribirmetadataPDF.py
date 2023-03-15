# De la librería PyPDF2, importamos PdfReader y PdfWriter
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("archivo1.pdf") # Indicamos el nombre del archivo que vamos a leer
writer = PdfWriter() # Creamos el objecto para crear nuestro archivo PDF y su metadata

# Añadimos todo el contenido del PDF previo al PDF nuevo
for page in reader.pages:
    writer.add_page(page) # con el add_page agregamos cada contenido que page encuentra

# añadimos la metadata
writer.add_metadata(
    {
        "/Author": "Bright Labs",
        "/Producer": "Bright Labs",
        "/Subject": "Escribir metadata",
        "/Title": "Escribir Metadata",
    }
)
# Guardamos el nuevo archivo PDF
with open("archivo_metadata.pdf", "wb") as f:
    writer.write(f)
    
#-----------------------------------------------------------------------------
# Utilizamos el mismo código para leer la metadata con el nuevo PDF
reader = PdfReader("archivo_metadata.pdf")
meta = reader.metadata
# Obtenemos la información del nuevo PDF
print(len(reader.pages)) # Imprimimos la cantidad de páginas
print(meta.author) # Imprimimos el nombre del autor
print(meta.producer) # Imprimimos el productor del PDF
print(meta.subject) # Imprimimos el asunto del PDF
print(meta.title) # Imprimimos el titulo del PDF