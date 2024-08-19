import os
from PIL import Image

ruta = input('\ningresa la ruta de una imagen para mostrarla y crear una copia\n\n')
img = Image.open(ruta)
img.show()
icq = input('\ndesea crear uan copia de forma persistente de esta imagen?\n\n(S/N)   ')
if icq == 'S':
    ruta2 = os.path.join(os.path.expanduser('~/Escritorio'), f'copia_{os.path.basename(ruta)}')
    copia = img.copy()
    copia.save(ruta2)
    print('\nla copia a sido creada exitosamente')
elif icq == 'N':
    VaribaleSinFuncion = 'si'
else:
    print('\nla respuesta no es valida')