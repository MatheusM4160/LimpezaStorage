import cv2
import numpy as np
from PIL import Image
import os

imagem1 = 'TOTEM FORMATURA.tif'

imagem2 = 'TOTEM CHARMANDER.tif'

# Carregar imagens com PIL
tamanho_img1 = Image.open(imagem1)
width1, height1 = tamanho_img1.size

# Carregar as mesmas imagens com OpenCV
img1 = cv2.imread(imagem1)

# Carregar imagem 2
tamanho_img2 = Image.open(imagem2)
width2, height2 = tamanho_img2.size

# Carregar imagem 2 com OpenCV
img2 = cv2.imread(imagem2)

print(f"Imagem 1 - Largura: {width1}px, Altura: {height1}px")
print(f"Imagem 2 - Largura: {width2}px, Altura: {height2}px")

# Comparação do tamanho das imagens
area_img1 = width1 * height1
area_img2 = width2 * height2

if area_img2 < area_img1:
    print('Imagem 2 é menor que a imagem 1')
    if width2 > height2:
        novo_width = int((width2 * height1) / height2)
        redirencionamento = tamanho_img2.resize((novo_width, height1))
        width2, height2 = redirencionamento.size
        print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        best_match = None
        best_match_score = 0
        for x in range(width2 - width1 + 1):
            sublimagem = redirencionamento[:, x:x + width1]

            elementos_iguais = np.sum(img1 == sublimagem)
            total_elementos = height1 * width1 * 3
            percentual_semelhante = (elementos_iguais / total_elementos) * 100

            if percentual_semelhante > best_match_score:
                best_match_score = percentual_semelhante
                best_match = (x, 0)
        if best_match_score >= 75:
            print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
        else:
            print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

    elif width2 < height2:
        novo_height = int((height2 * width1) / width2)
        redirencionamento = tamanho_img2.resize((width1, novo_height))
        width2, height2 = redirencionamento.size
        print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        best_match = None
        best_match_score = 0
        for y in range(height2 - height1 + 1):
            sublimagem = redirencionamento[y:y + height1, :]

            elementos_iguais = np.sum(img1 == sublimagem)
            total_elementos = height1 * width1 * 3
            percentual_semelhante = (elementos_iguais / total_elementos) * 100

            if percentual_semelhante > best_match_score:
                best_match_score = percentual_semelhante
                best_match = (0, y)
        if best_match_score >= 75:
            print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
        else:
            print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

    else:
        if width1 >= height1:
            redirencionamento = tamanho_img2.resize((width1, width1))
            width2, height2 = redirencionamento.size
            print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")
        else:
            redirencionamento = tamanho_img2.resize((height1, height1))
            width2, height2 = redirencionamento.size
            print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        total_elementos = width1 * height1 * 3
    
        elementos_iguais = np.sum(img1 == redirencionamento)
        percentual_semelhante = (elementos_iguais / total_elementos) * 100

        if percentual_semelhante >= 75:
            print(f'As imagens são Semelhantes em {percentual_semelhante}%')
        else:
            print('As imagens não são semelhantes em mais ou igual a 75%')

    


elif area_img2 > area_img1:
    print('Imagem 2 é maior que a imagem 1')
    if width2 > height2:
        novo_width = int((width2 * height1) / height2)
        redirencionamento = tamanho_img2.resize((novo_width, height1))
        width2, height2 = redirencionamento.size
        print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        best_match = None
        best_match_score = 0
        for x in range(width2 - width1 + 1):
            sublimagem = redirencionamento[:, x:x + width1]

            elementos_iguais = np.sum(img1 == sublimagem)
            total_elementos = height1 * width1 * 3
            percentual_semelhante = (elementos_iguais / total_elementos) * 100

            if percentual_semelhante > best_match_score:
                best_match_score = percentual_semelhante
                best_match = (x, 0)
        if best_match_score >= 75:
            print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
        else:
            print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

    elif width2 < height2:
        novo_height = int((height2 * width1) / width2)
        redirencionamento = tamanho_img2.resize((width1, novo_height))
        width2, height2 = redirencionamento.size
        print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        best_match = None
        best_match_score = 0
        for y in range(height2 - height1 + 1):
            sublimagem = redirencionamento[y:y + height1, :]

            elementos_iguais = np.sum(img1 == sublimagem)
            total_elementos = height1 * width1 * 3
            percentual_semelhante = (elementos_iguais / total_elementos) * 100

            if percentual_semelhante > best_match_score:
                best_match_score = percentual_semelhante
                best_match = (0, y)
        if best_match_score >= 75:
            print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
        else:
            print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

    else:
        if width1 >= height1:
            redirencionamento = tamanho_img2.resize((width1, width1))
            width2, height2 = redirencionamento.size
            print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")
        else:
            redirencionamento = tamanho_img2.resize((height1, height1))
            width2, height2 = redirencionamento.size
            print(f"Redimensionada: Largura: {width2}px, Altura: {height2}px")

        redirencionamento = np.array(redirencionamento)
        total_elementos = width1 * height1 * 3
    
        elementos_iguais = np.sum(img1 == redirencionamento)
        percentual_semelhante = (elementos_iguais / total_elementos) * 100

        if percentual_semelhante >= 75:
            print(f'As imagens são Semelhantes em {percentual_semelhante}%')
        else:
            print('As imagens não são semelhantes em mais ou igual a 75%')



else:
    print('As imagens têm o mesmo tamanho')
    total_elementos = img1.size
    
    elementos_iguais = np.sum(img1 == img2)
    percentual_semelhante = (elementos_iguais / total_elementos) * 100

    if percentual_semelhante >= 75:
        print(f'As imagens são Semelhantes em {percentual_semelhante}%')
    else:
        print('As imagens não são semelhantes em mais ou igual a 75%')