def PesquisaStorage(CaminhaPrincipal, CaminhoSimilar, CaminhoProcessados):
    import os
    import shutil
    import scaner_similar

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
        caminho_referencia = os.path.join(CaminhaPrincipal, arquivo_referencia)

        print(f'Processando referencia {arquivo_referencia}.')

        # Loop para verificar todos os arquivos da pasta
        for arquivo in arquivos[1:]:
            caminho_arquivo = os.path.join(CaminhaPrincipal, arquivo)

            resultado = scaner_similar.ScanerSimilar(Diretorio1=caminho_referencia, Diretorio2=caminho_arquivo, Image1=arquivo_referencia, Image2=arquivo)

            # Verifica se o conteudo de resultado é 'Semelhante' ou 'Difetente'
            if resultado == 'Semelhantes':
                print(f'Imagem {arquivo} é similar')
                shutil.move(caminho_arquivo, os.path.join(CaminhoSimilar, arquivo))
            else:
                print(f'Imagem {arquivo} é diferente')
        
        # Após verificar todos os arquivos move o arquivo de referencia para uma pasta separada e volta o para o topo do Loop
        shutil.move(caminho_referencia, os.path.join(CaminhoProcessados, arquivo_referencia))