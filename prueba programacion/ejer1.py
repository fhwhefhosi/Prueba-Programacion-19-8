import os
from PIL import Image

ruta = input('\ningrese la ruta de una imagen para mostrarla y ver sus datos\n\n')
img = Image.open(ruta)
img.show()
print('-'*75)
print(f'|nombre de la imagen |{os.path.basename(ruta)}'
      f'\n|formato             |{img.format}'
      f'\n|resolucion          |{img.size}'
      f'\n|pixeles totales     |{img.width * img.height}'
      f'\n|ruta de la imagen   |{ruta}')
print('-'*75)
