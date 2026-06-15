EPUB Combiner

Herramienta en Python para combinar múltiples archivos EPUB en un único libro, manteniendo el orden según los números presentes en los nombres de los archivos.

Características.
* Detecta automáticamente todos los archivos epub de la carpeta actual.
* Ordena los EPUB según el número encontrado en el nombre del archivo.
* Extrae el contenido HTML de cada libro.
* Genera un único archivo EPUB combinado.
* Crea automáticamente la tabla de contenidos y la navegación del libro resultante.

Requisitos para ejecución del script:
* Python 3.8 o superior
* EbookLib

Instalación:
pip install ebooklib

Uso
1. Coloca todos los archivos epub que deseas combinar en la misma carpeta que el script.
2. Asegúrate de que los nombres contengan números para indicar el orden, por ejemplo:

Capitulo_1.epub
Capitulo_2.epub
Capitulo_3.epub

3. Ejecuta el script:
python combinar_epub.py

4. Se generará el archivo:
Libro_Completo.epub

Ejemplo de salida:

Orden detectado:
Capitulo_1.epub
Capitulo_2.epub
Capitulo_3.epub

EPUB combinado creado: Libro_Completo.epub

