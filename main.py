import pesquisa_storage
Principal = input('Caminho Principal: ')
Similares = input('Caminho Similares: ')
Processados = input('Caminho Processados: ')

pesquisa_storage.PesquisaStorage(CaminhaPrincipal=Principal,
                                 CaminhoSimilar=Similares,
                                 CaminhoProcessados=Processados)