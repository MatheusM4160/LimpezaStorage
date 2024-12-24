import flet as ft
from mapear import mape


def main(page):
    def fechar(e):
        if Erro.open == True:
            Erro.open = False
            page.update()

    botao_fechar = ft.ElevatedButton('Fechar', on_click=fechar)
    Erro = ft.AlertDialog(title='Erro', content='Informação Inválida', actions=[botao_fechar])

    Titulo = ft.Text('Limpeza Storage', size=20)
    page.add(Titulo)

    def mapear_arquivos(e):
        page.remove(Titulo, botao_mapear)
        def sair(e):
            page.remove(botao_voltar)
            page.remove(acoes)
            page.add(Titulo)
            page.add(botao_mapear)

        def mapear(e):
            try:
                str(caminho_diretorio.value)
            except:
                Erro.open = True
                page.add(Erro)
            else:
                if caminho_diretorio.value != '':
                    mape(caminho_diretorio.value)
                else:
                    Erro.open = True
                    page.add(Erro)

        
        botao_voltar = ft.ElevatedButton('Voltar', on_click=sair)
        page.add(botao_voltar)

        caminho_diretorio = ft.TextField(label='Caminho para mapear')
        start = ft.ElevatedButton('Start', on_click=mapear)
        acoes = ft.Row([caminho_diretorio, start])
        page.add(acoes)
        

    botao_mapear = ft.ElevatedButton('Mapear Arquivos', on_click=mapear_arquivos)
    page.add(botao_mapear)


ft.app(main)