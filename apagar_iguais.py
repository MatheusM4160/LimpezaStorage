import json
import os

with open('armazenamento.json', 'r') as file:
    lista = json.load(file)


for x in lista:
    if x["Novo Diretorio"] is not None:
        path1 = os.path.join(x["Novo Diretorio"])
        os.remove(path1)
        path2 = os.path.join(x["Diretorio Arquivo"])
        os.remove(path2)
        print('Removido com sucesso!')

print('pronto!')