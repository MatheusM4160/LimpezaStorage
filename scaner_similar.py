def ResizeImagePil(Img, new_width, new_height):
    from PIL import Image
    import numpy as np
    pil_image = Image.fromarray(Img)
    resized_image = pil_image.resize((new_width, new_height))
    return np.array(resized_image)


def ScanerSimilar(Diretorio1, Diretorio2):
    import numpy as np
    import os
    import imageio.v3 as iio
    

    Imagem1 = Diretorio1
    Imagem2 = Diretorio2
    
    # Carregar imagens com PIL para pegar os tamanhos
    img1 = iio.imread(Imagem1)  # Imagem 1 em escala de cinza

    img2 = iio.imread(Imagem2)  # Imagem 2 em escala de cinza

    if len(img1.shape) == 3:  # Verifica se a imagem tem 3 canais (RGB)
        img1 = np.dot(img1[..., :3], [0.2989, 0.5870, 0.1140])  # Conversão para tons de cinza
    if len(img2.shape) == 3:
        img2 = np.dot(img2[..., :3], [0.2989, 0.5870, 0.1140])

    height1, width1 = img1.shape
    height2, width2 = img2.shape

    print(f"Imagem 1 - Largura: {width1}px, Altura: {height1}px")
    print(f"Imagem 2 - Largura: {width2}px, Altura: {height2}px")

    area_img1 = height1 * width1
    area_img2 = height2 * width2

    # Caso as imagens tenham o mesmo tamanho
    if (width1, height1) == (width2, height2):
        print('As imagens têm o mesmo tamanho')
        total_elementos = img1.size
        
        elementos_iguais = np.sum(img1 == img2) # Comparar valores pixel a pixel
        percentual_semelhante = (elementos_iguais / total_elementos) * 100 # Número total de pixels

        if percentual_semelhante >= 75:
            print(f'As imagens são Semelhantes em {percentual_semelhante}%')
            return 'Semelhantes'
        else:
            print('As imagens não são semelhantes em mais ou igual a 75%')
            return 'Diferentes'
        
    

    # Compara os tamanhos
    else:
        if area_img2 > area_img1:
            print('O tamanho da imagem 2 é Maior que a imagem 1')

            # Redimensionar imagem 2 para ter a mesma altura da imagem 1, mantendo proporção
            if width2 > height2:
                novo_width = int((width2 * height1) / height2)
                redirencionamento = ResizeImagePil(img2, novo_width, height1)
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
                    return 'Semelhantes'
                else:
                    print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                    return 'Diferentes'

            # Redimensionar imagem 2 para ter a mesma largura da imagem 1, mantendo proporção
            elif width2 < height2:
                novo_height = int((height2 * width1) / width2)
                redirencionamento = ResizeImagePil(img2, width1, novo_height)
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
                    return 'Semelhantes'
                else:
                    print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                    return 'Diferentes'

            # Caso a imagem seja quadrada
            else:
                # Redimensiona a imamgem 2 para ter a mesma largura da imagem 1, caso a largura seja maior ou igual que a altura
                if width1 >= height1:
                    redirencionamento = ResizeImagePil(img2, width1, width1)
                    print(f"Redimensionada: Largura: {width1}px, Altura: {width1}px")

                    redirencionamento = np.array(redirencionamento)
                    best_match = None
                    best_match_score = 0

                    # Comparar partes da imagem 2 com a imagem 1 verticalmente
                    for y in range(width1 - height1 + 1):
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
                        return 'Semelhantes'
                    else:
                        print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                        return 'Diferentes'

                # Redimensiona a imamgem 2 para ter a mesma altura da imagem 1, caso a altura seja menor que a altura
                else:
                    redirencionamento = ResizeImagePil(img2, height1, height1)
                    print(f"Redimensionada: Largura: {height1}px, Altura: {height1}px")

                    redirencionamento = np.array(redirencionamento)
                    best_match = None
                    best_match_score = 0

                    # Comparar partes da imagem 2 com a imagem 1 horizontalmente
                    for x in range(height1 - width1 + 1):
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
                        return 'Semelhantes'
                    else:
                        print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                        return 'Diferentes'
                    

        else:
            print('O tamanho da imagem 2 é Menor que a imagem 1')

            # Redimensionar imagem 1 para ter a mesma altura da imagem 2, mantendo proporção
            if width1 > height1:
                novo_width = int((width1 * height2) / height1)
                redirencionamento = ResizeImagePil(img1, novo_width, height2)
                print(f"Redimensionada: Largura: {novo_width}px, Altura: {height2}px")

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
                    return 'Semelhantes'
                else:
                    print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                    return 'Diferentes'

            # Redimensionar imagem 1 para ter a mesma largura da imagem 2, mantendo proporção
            elif width1 < height1:
                novo_height = int((height1 * width2) / width1)
                redirencionamento = ResizeImagePil(img1, width2, novo_height)
                print(f"Redimensionada: Largura: {width2}px, Altura: {novo_height}px")

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
                    return 'Semelhantes'
                else:
                    print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                    return 'Diferentes'

            # Caso a imagem seja quadrada
            else:
                # Redimensiona a imamgem 1 para ter a mesma largura da imagem 2, caso a largura seja maior ou igual que a altura
                if width2 >= height2:
                    redirencionamento = ResizeImagePil(img1, width2, width2)
                    print(f"Redimensionada: Largura: {width2}px, Altura: {width2}px")

                    redirencionamento = np.array(redirencionamento)
                    best_match = None
                    best_match_score = 0

                    # Comparar partes da imagem 2 com a imagem 1 verticalmente
                    for y in range(width1 - height1 + 1):
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
                        return 'Semelhantes'
                    else:
                        print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                        return 'Diferentes'

                # Redimensiona a imamgem 1 para ter a mesma altura da imagem 2, caso a altura seja menor que a altura
                else:
                    redirencionamento = ResizeImagePil(img1, height2, height2)
                    print(f"Redimensionada: Largura: {height2}px, Altura: {height2}px")

                    redirencionamento = np.array(redirencionamento)
                    best_match = None
                    best_match_score = 0

                    # Comparar partes da imagem 2 com a imagem 1 horizontalmente
                    for x in range(height1 - width1 + 1):
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
                        return 'Semelhantes'
                    else:
                        print(f'Nenhum match superior a 75% encontrado. {best_match_score:.2f}%')
                        return 'Diferentes'