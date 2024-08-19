import os
from PIL import Image

ruta = input('\nBienvenido, ingresa la ruta de una imagen para mostrarla y agregarle una marca de agua\n\n')
img = Image.open(ruta)
img.show()
icq = input('\ndesea agregarle una marca de agua a esta imagen?\n\n(S/N)   ')
if icq == 'S':
    rutaIDA = input('\ningrese la ruta de la imagen de agua\n\n')
    img2 = Image.open(rutaIDA)
    marcaDeAgua = img2.resize((75,75))
    ruta2 = os.path.join(os.path.expanduser('~/Escritorio'), f'marca_de_agua_{os.path.basename(ruta)}')
    ldm = input('\nen que lugar deseas poner la marca de agua?'
                '\n1 --- esquina superior izquierda'
                '\n2 --- esquina supeior derecha'
                '\n3 --- esquina inferior izquierda'
                '\n4 --- esquina inferior derecha\n\n')
    if ldm == '1':
        x = 50 
        y = 50
    elif ldm == '2':
        x = img.width - 50 - marcaDeAgua.width
        y = 50
    elif ldm == '3':
        x = 50
        y = img.height - 50 - marcaDeAgua.height
    elif ldm == '4':
        x = img.width - 50 - marcaDeAgua.width
        y = img.height - 50 - marcaDeAgua.height
    else:
        print('la opcion es invalida')
    img.paste(marcaDeAgua,(x,y),marcaDeAgua.convert('RGBA'))
    img.save(ruta2)
    print('\nla imagen asido creada exitosamente\n')
elif icq == 'N':
    VariableSinFuncion = 0*0
else:
    print('\nla opcion es invalida')