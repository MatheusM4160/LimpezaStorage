import os

path = "W:\\MATHEUS PAINIES SUBLIMA\u00c7\u00c3O 2024\\MATHEUS\\destino miniaturas\\bolsinha__05.bmp"

try:
    os.path.join(path)
except:
    print('Deu ruim!')
else:
    print('Deu certo!')