import os
import re
from ebooklib import epub

def obtener_numero(nombre):
    match = re.search(r'\d+', nombre)
    return int(match.group()) if match else 0

# Obtener lista de epub
archivos = [f for f in os.listdir('.') if f.endswith('.epub')]

# Ordenarlos por el número en el nombre
archivos.sort(key=obtener_numero)

print("Orden detectado:")
for a in archivos:
    print(a)

# Crear nuevo epub
libro_final = epub.EpubBook()
libro_final.set_title('Libro Completo')
libro_final.set_language('es')

contenido_total = []
contador_cap = 1

for archivo in archivos:
    libro = epub.read_epub(archivo)

    for item in libro.get_items():
        if item.get_type() == 9:  # Documento HTML
            cap = epub.EpubHtml(
                title=f'Capítulo {contador_cap}',
                file_name=f'cap_{contador_cap}.xhtml',
                content=item.get_content()
            )
            libro_final.add_item(cap)
            contenido_total.append(cap)
            contador_cap += 1

libro_final.toc = tuple(contenido_total)
libro_final.add_item(epub.EpubNcx())
libro_final.add_item(epub.EpubNav())

libro_final.spine = ['nav'] + contenido_total

epub.write_epub('Libro_Completo.epub', libro_final)

print("EPUB combinado creado: Libro_Completo.epub")