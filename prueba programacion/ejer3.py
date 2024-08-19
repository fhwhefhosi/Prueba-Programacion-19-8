import os
from PIL import Image

ruta = input('\ningresa la ruta de una imagen\n\n')
rot = int(input('\ningresa la rotacion que deseas\n\n'))
img = Image.open(ruta)
img.show()
icq = input('\ndeseas crear una copia con la rotacion elegida?\n\n(S/N)   ')
if icq == 'S':
    base, ext = os.path.splitext(ruta)
    ruta2 = os.path.join(os.path.expanduser('~/Escritorio'), f'{base}rot{ext}')
    imgrot = img.copy()
    imgrot.rotate(rot, expand=True).save(ruta2)
    imgrot = Image.open(ruta2)
    imgrot.show()
elif icq == 'N':
    VariableSinFuncion = 0
else:
    print('la opcion es invalida')