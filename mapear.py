import os
import json
import functools

lista = []

with open('armazenamento.json', 'r') as file:
    try:
        lista = json.load(file)
    except json.JSONDecodeError:
        lista = []

@functools.lru_cache()
def mapear(diretorio):
    for raiz, _, arquivos, in os.walk(diretorio):
        for arquivo in os.listdir(raiz):
            if '.' in arquivo:  
                print(arquivo)
                caminho_referencia = os.path.join(raiz, arquivo)

                print(caminho_referencia) 
                dic = {
                    'Nome Arquivo': arquivo,
                    'Diretorio Arquivo': caminho_referencia
                    }
                lista.append(dic)
                #dic.clear()

diretorio = input('Caminho: ')
mapear(diretorio)

print(lista)
with open('armazenamento.json', 'w') as file:
    json.dump(lista, file, indent=4)