from PIL import Image, ImageChops
import numpy as np

def compare_images(image_path1, image_path2):
    """
    Compara duas imagens e retorna se elas são idênticas e o nível de semelhança.

    Args:
        image_path1 (str): Caminho para a primeira imagem.
        image_path2 (str): Caminho para a segunda imagem.

    Returns:
        bool: True se as imagens forem idênticas, False caso contrário.
        float: Porcentagem de semelhança entre as imagens (0 a 100).
    """
    # Abrir as imagens
    try:
        image1 = Image.open(image_path1).convert("RGB")
        image2 = Image.open(image_path2).convert("RGB")
    except:
        print('Não foi possivel abrir as imagens!')
    else:

        print(image1.size, image2.size)

        # Verificar se as dimensões das imagens são iguais
        if image1.size != image2.size:
            raise ValueError("As imagens precisam ter o mesmo tamanho para serem comparadas.")

        # Calcular a diferença entre as imagens
        diff = ImageChops.difference(image1, image2)

        # Converter a diferença para um array NumPy
        diff_array = np.array(diff, dtype=np.float32)

        # Calcular a soma total das diferenças (em R, G, B)
        total_diff = np.sum(diff_array)

        # Calcular o valor máximo possível de diferença
        max_diff = image1.size[0] * image1.size[1] * 255 * 3

        # Calcular a porcentagem de semelhança
        similarity = 100 - (total_diff / max_diff * 100)

        # Verificar se as imagens são idênticas
        identical = similarity == 100

        return identical, similarity