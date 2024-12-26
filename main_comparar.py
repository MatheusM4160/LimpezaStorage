from comparar import compare_images
import json
import os
import shutil
import functools

with open('armazenamento.json', 'r') as file:
    try:
        lista = json.load(file)
    except:
        print('Não foi possível ler a lista!')

@functools.lru_cache()
def mapear():
    for x in lista:
        for y in lista:
            if x["Nome Arquivo"] != y["Nome Arquivo"] and y['Diretorio Miniatura'] is not None and x['Diretorio Miniatura'] is not None:
                print(x["Nome Arquivo"], y["Nome Arquivo"])
                try:
                    identical, similarity = compare_images(image_path1=x["Diretorio Miniatura"], image_path2=y["Diretorio Miniatura"])
                except:
                    continue
                else:
                    if identical == True:
                        shutil.move(os.path.join(y['Diretorio Miniatura']), os.path.join('W:/MATHEUS PAINIES SUBLIMAÇÃO 2024/MATHEUS/similares'))
                        __,n = os.path.split(y['Diretorio Arquivo'])
                        y['Novo Diretorio'] = 'W:/MATHEUS PAINIES SUBLIMAÇÃO 2024/MATHEUS/similares' + f'/{n.replace('tif','bmp')}'
                        print(f'Imagem {x['Nome Arquivo']} é igual a imagem {y['Nome Arquivo']}!')
                    else:
                        print('Imagens diferentes!')

mapear()