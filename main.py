import scaner_similar

scaner_similar.ScanerSmilar()

def PesquisaStorage(CaminhaPrincipal, CaminhoSimilar, CaminhoProcessados):
    import os
    import shutil

    # Cria os diretórios de imagens similares e processadas caso não exista
    os.makedirs(CaminhoSimilar, exist_ok=True)
    os.makedirs(CaminhoProcessados, exist_ok=True)

    while True:
        # Lista os arquivos da pasta
        arquivos = os.listdir(CaminhaPrincipal)
        if not arquivos:
            print("Nenhuma imagem restante na pasta principal.")
            break

        # Seleciona a primeira imagem como referencia
        arquivo_referencia = arquivos[0]