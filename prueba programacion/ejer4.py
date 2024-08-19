import os
from PIL import Image

name_img = input('\nBienvenido, ingresa el nombre de una imagen de tu escritorio para mostrarla y recosrtarla\n\n')
img = Image.open(os.path.expanduser(f'~/Escritorio/{name_img}'))
img.show()
icq = input('\ndesea realizar un recorte a esta imagen?(se creara una carpeta de recortes)\n\n(S/N)   ')
if icq == 'S':
    if not os.path.exists(f'~/Escritorio/recortes'):
        os.mkdir(os.path.expanduser('~/Escritotio/recortes'))
    i = 0
    while True:
        i += 1
        if os.path.exists(os.path.expanduser(f'~/Escritorio/recortes/recorte_{i}.png')):
            continue
        else:
            nombre = f'recorte_{i}'
            break
    ruta2 = os.path.join(os.path.expanduser('~/Escritorio/recortes'), f'{nombre}.png')
    print(img.size,'   estos datos son los datos de la resolucion de la imagen')
    x1 = int(input('\ningrese una cordenada en x inicial\n\n'))
    y1 = int(input('\ningrese una cordenada en y inicial\n\n'))
    x2 = int(input('\ningrese el ancho del recorte\n\n'))
    y2 = int(input('\ningrese el alto del recorte\n\n'))
    if x1 + x2 > img.width or y1 + y2 > img.height:
        print('\nlos datos proporsionados soninvalidos\n')
        quit()
    recorte = img.crop((x1,y2,x1+x2,y1+y2))
    recorte.save(ruta2)
    print('\nel recorte a sido creado con exito\n')
elif icq == 'N':
    VariableSinFuncion = 1*1
else:
    print('\nla opcion es invalida')