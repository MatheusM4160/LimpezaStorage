import json
import imageio.v3 as iio
from resizer import create_thumbnail

lista = []

with open('armazenamento.json', 'r') as file:
    try:
        lista = json.load(file)
    except json.JSONDecodeError:
        lista = []

for x in lista:
    try:
        img1 = iio.imread(x['Diretorio Arquivo'])
        height1, width1, _ = img1.shape
        print(x['Diretorio Arquivo'])
        print(height1, width1)
    except:
        pass
    else:
        if height1 == width1:
            create_thumbnail(filename=x['Diretorio Arquivo'], path_dest='W:/MATHEUS PAINIES SUBLIMAÇÃO 2024/MATHEUS/destino miniaturas')
        elif height1 > width1:
            # height1 = 640
            create_thumbnail(filename=x['Diretorio Arquivo'], path_dest='W:/MATHEUS PAINIES SUBLIMAÇÃO 2024/MATHEUS/destino miniaturas', size=((width1*640)/height1, 640))
        else:
            # width1 = 640
            create_thumbnail(filename=x['Diretorio Arquivo'], path_dest='W:/MATHEUS PAINIES SUBLIMAÇÃO 2024/MATHEUS/destino miniaturas', size=(640, (height1*640)/width1))