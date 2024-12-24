import json
import imageio.v3 as iio
from resizer import create_thumbnail

destino = str(input('Caminho: '))

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
        diretorio_miniatura = create_thumbnail(filename=x['Diretorio Arquivo'], path_dest=destino)
        x['Diretorio Miniatura'] = diretorio_miniatura
        print('Sucesso')
        
with open('armazenamento.json', 'w') as file:
    json.dump(lista, file, indent=4)