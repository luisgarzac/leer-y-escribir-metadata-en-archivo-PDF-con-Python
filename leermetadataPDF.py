# Vamos a leer la metadata de un archivo PDF en nuestra computadora
from PyPDF2 import PdfReader # De la librería importamos PdfReader

reader = PdfReader("archivo1.pdf") # con la función PdfReader indicamos el nombre del archivo

meta = reader.metadata # a la variable reader le decimos que queremos su metadata

print(len(reader.pages)) # Imprimimos la cantidad de páginas
print(meta.author) # Imprimimos el nombre del autor
print(meta.creator) # Imprimimos la aplicación con la que fue creado el PDF
print(meta.producer) # Imprimimos el productor del PDF
print(meta.subject) # Imprimimos el asunto del PDF
print(meta.title) # Imprimimos el titulo del PDF
