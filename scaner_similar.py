def ScanerSmilar(Image1, Imagem2):
    import cv2
    import numpy as np
    from PIL import Image

    # Carregar imagens com PIL para pegar os tamanhos
    tamanho_img1 = Image.open(Image1)
    width1, height1 = tamanho_img1.size

    # Carregar as mesmas imagens com OpenCV para pegar a matriz em escala de cinza
    img1 = cv2.imread(Image1, cv2.IMREAD_GRAYSCALE)

    # Carregar imagem 2 com PIL para pegar os tamanhos
    tamanho_img2 = Image.open(Imagem2)
    width2, height2 = tamanho_img2.size

    # Carregar imagem 2 com OpenCV para pegar com a matriz em escala de cinza
    img2 = cv2.imread(Imagem2, cv2.IMREAD_GRAYSCALE)

    print(f"Imagem 1 - Largura: {width1}px, Altura: {height1}px")
    print(f"Imagem 2 - Largura: {width2}px, Altura: {height2}px")

    # Pegar a area de cada imagem
    area_img1 = width1 * height1
    area_img2 = width2 * height2

    # Compara os tamanhos
    if area_img2 < area_img1:
        print('Imagem 2 é menor que a imagem 1')

        # Redimensionar imagem 2 para ter a mesma altura da imagem 1, mantendo proporção
        if width2 > height2:
            novo_width = int((width2 * height1) / height2)
            redirencionamento = cv2.resize(img2, (novo_width, height1))
            print(f"Redimensionada: Largura: {novo_width}px, Altura: {height1}px")

            redirencionamento = np.array(redirencionamento)
            best_match = None
            best_match_score = 0

            # Comparar partes da imagem 2 com a imagem 1 horizontalmente
            for x in range(novo_width - width1 + 1):
                sublimagem = redirencionamento[:, x:x + width1] # Fatia da imagem 2 com a largura da imagem 1

                elementos_iguais = np.sum(img1 == sublimagem) # Comparar valores pixel a pixel
                total_elementos = height1 * width1 # Número total de pixels
                percentual_semelhante = (elementos_iguais / total_elementos) * 100

                # Caso o percentual semelhate seja maior que a maior semelhança encontrada vai mudar seu valor antigo
                if percentual_semelhante > best_match_score:
                    best_match_score = percentual_semelhante
                    best_match = (x, 0)

            if best_match_score >= 75:
                print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
            else:
                print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

        # Redimensionar imagem 2 para ter a mesma largura da imagem 1, mantendo proporção
        elif width2 < height2:
            novo_height = int((height2 * width1) / width2)
            redirencionamento = cv2.resize(img2, (width1, novo_height))
            print(f"Redimensionada: Largura: {width1}px, Altura: {novo_height}px")

            redirencionamento = np.array(redirencionamento)
            best_match = None
            best_match_score = 0

            # Comparar partes da imagem 2 com a imagem 1 verticalmente
            for y in range(novo_height - height1 + 1):
                sublimagem = redirencionamento[y:y + height1, :] # Fatia da imagem 2 com a largura da imagem 1

                elementos_iguais = np.sum(img1 == sublimagem) # Comparar valores pixel a pixel
                total_elementos = height1 * width1 # Número total de pixels
                percentual_semelhante = (elementos_iguais / total_elementos) * 100

                # Caso o percentual semelhate seja maior que a maior semelhança encontrada vai mudar seu valor antigo
                if percentual_semelhante > best_match_score:
                    best_match_score = percentual_semelhante
                    best_match = (0, y)

            if best_match_score >= 75:
                print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
            else:
                print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

        # Caso a imagem seja quadrada
        else:
            # Redimensiona a imamgem 2 para ter a mesma largura da imagem 1, caso a largura seja maior ou igual que a altura
            if width1 >= height1:
                redirencionamento = cv2.resize(img2, (width1, width1))
                print(f"Redimensionada: Largura: {width1}px, Altura: {width1}px")

            # Redimensiona a imamgem 2 para ter a mesma altura da imagem 1, caso a altura seja menor que a altura
            else:
                redirencionamento = cv2.resize(img2, (height1, height1))
                print(f"Redimensionada: Largura: {height1}px, Altura: {height1}px")

            redirencionamento = np.array(redirencionamento)
            total_elementos = width1 * height1
        
            elementos_iguais = np.sum(img1 == redirencionamento) # Comparar valores pixel a pixel
            percentual_semelhante = (elementos_iguais / total_elementos) * 100 # Número total de pixels

            if percentual_semelhante >= 75:
                print(f'As imagens são Semelhantes em {percentual_semelhante}%')
            else:
                print('As imagens não são semelhantes em mais ou igual a 75%')

        

    # Compara os tamanhos
    elif area_img2 > area_img1:
        print('Imagem 2 é maior que a imagem 1')

        # Redimensionar imagem 2 para ter a mesma altura da imagem 1, mantendo proporção
        if width2 > height2:
            novo_width = int((width2 * height1) / height2)
            redirencionamento = cv2.resize(img2, (novo_width, height1))
            print(f"Redimensionada: Largura: {novo_width}px, Altura: {height1}px")

            redirencionamento = np.array(redirencionamento)
            best_match = None
            best_match_score = 0

            # Comparar partes da imagem 2 com a imagem 1 horizontalmente
            for x in range(novo_width - width1 + 1):
                sublimagem = redirencionamento[:, x:x + width1] # Fatia da imagem 2 com a largura da imagem 1

                elementos_iguais = np.sum(img1 == sublimagem) # Comparar valores pixel a pixel
                total_elementos = height1 * width1 # Número total de pixels
                percentual_semelhante = (elementos_iguais / total_elementos) * 100

                # Caso o percentual semelhate seja maior que a maior semelhança encontrada vai mudar seu valor antigo
                if percentual_semelhante > best_match_score:
                    best_match_score = percentual_semelhante
                    best_match = (x, 0)

            if best_match_score >= 75:
                print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
            else:
                print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

        # Redimensionar imagem 2 para ter a mesma largura da imagem 1, mantendo proporção
        elif width2 < height2:
            novo_height = int((height2 * width1) / width2)
            redirencionamento = cv2.resize(img2, (width1, novo_height))
            print(f"Redimensionada: Largura: {width1}px, Altura: {novo_height}px")

            redirencionamento = np.array(redirencionamento)
            best_match = None
            best_match_score = 0

            # Comparar partes da imagem 2 com a imagem 1 verticalmente
            for y in range(novo_height - height1 + 1):
                sublimagem = redirencionamento[y:y + height1, :] # Fatia da imagem 2 com a largura da imagem 1

                elementos_iguais = np.sum(img1 == sublimagem) # Comparar valores pixel a pixel
                total_elementos = height1 * width1 # Número total de pixels
                percentual_semelhante = (elementos_iguais / total_elementos) * 100
                
                # Caso o percentual semelhate seja maior que a maior semelhança encontrada vai mudar seu valor antigo
                if percentual_semelhante > best_match_score:
                    best_match_score = percentual_semelhante
                    best_match = (0, y)

            if best_match_score >= 75:
                print(f'Match encontrado! As imagens são semelhantes em {best_match_score:.2f}% na posição {best_match}')
            else:
                print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')

        # Caso a imagem seja quadrada
        else:
            # Redimensiona a imamgem 2 para ter a mesma largura da imagem 1, caso a largura seja maior ou igual que a altura
            if width1 >= height1:
                redirencionamento = cv2.resize(img2, (width1, width1))
                print(f"Redimensionada: Largura: {width1}px, Altura: {width1}px")
            
            # Redimensiona a imamgem 2 para ter a mesma altura da imagem 1, caso a altura seja menor que a altura
            else:
                redirencionamento = cv2.resize(img2, (height1, height1))
                print(f"Redimensionada: Largura: {height1}px, Altura: {height1}px")

            redirencionamento = np.array(redirencionamento)
            total_elementos = width1 * height1
        
            elementos_iguais = np.sum(img1 == redirencionamento) # Comparar valores pixel a pixel
            percentual_semelhante = (elementos_iguais / total_elementos) * 100 # Número total de pixels

            if percentual_semelhante >= 75:
                print(f'As imagens são Semelhantes em {percentual_semelhante}%')
            else:
                print('As imagens não são semelhantes em mais ou igual a 75%')



    # Caso a imagem seja quadrada
    else:
        print('As imagens têm o mesmo tamanho')
        total_elementos = img1.size
        
        elementos_iguais = np.sum(img1 == img2) # Comparar valores pixel a pixel
        percentual_semelhante = (elementos_iguais / total_elementos) * 100 # Número total de pixels

        if percentual_semelhante >= 75:
            print(f'As imagens são Semelhantes em {percentual_semelhante}%')
        else:
            print('As imagens não são semelhantes em mais ou igual a 75%')