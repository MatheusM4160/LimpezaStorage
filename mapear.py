import os
import json

diretorio = input('Caminho: ')


lista = []

with open('armazenamento.json', 'r') as file:
    try:
        lista = json.load(file)
    except json.JSONDecodeError:
        lista = []


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


print(lista)
with open('armazenamento.json', 'w') as file:
    json.dump(lista, file, indent=4)