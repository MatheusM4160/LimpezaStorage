import os
import cv2
import shutil
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import normalize
from PIL import Image

def redimensionar_imagem(imagem, max_largura=1500, max_altura=1500):
    """
    Redimensiona a imagem para garantir que ela não ultrapasse os limites especificados.
    """
    altura, largura = imagem.shape[:2]
    
    if largura > max_largura or altura > max_altura:
        fator_redimensionamento = min(max_largura / largura, max_altura / altura)
        nova_largura = int(largura * fator_redimensionamento)
        nova_altura = int(altura * fator_redimensionamento)
        imagem_redimensionada = cv2.resize(imagem, (nova_largura, nova_altura))
        return imagem_redimensionada
    else:
        return imagem

def verificar_imagem_grande(imagem_path, limite_tamanho_mb=50):
    """
    Verifica se o tamanho do arquivo da imagem é maior do que o limite especificado (em MB).
    """
    tamanho_imagem = os.path.getsize(imagem_path) / (1024 * 1024)  # Tamanho em MB
    if tamanho_imagem > limite_tamanho_mb:
        print(f"Imagem {imagem_path} é muito grande ({tamanho_imagem:.2f} MB), pulando...")
        return False
    return True

def carregar_imagem(imagem_path, max_largura=1500, max_altura=1500):
    """
    Carrega e redimensiona a imagem se necessário.
    """
    try:
        # Usando o OpenCV para carregar a imagem
        imagem = cv2.imread(imagem_path)
        
        if imagem is None:
            print(f"Erro ao carregar a imagem: {imagem_path}")
            return None
        
        # Redimensiona a imagem se necessário
        imagem = redimensionar_imagem(imagem, max_largura, max_altura)
        
        return imagem
    except Exception as e:
        print(f"Erro ao carregar a imagem {imagem_path}: {e}")
        return None

def calcular_similaridade(imagem1, imagem2):
    """
    Calcula a similaridade entre duas imagens usando cosine similarity.
    """
    # Converte as imagens para vetores
    imagem1 = imagem1.flatten().reshape(1, -1)
    imagem2 = imagem2.flatten().reshape(1, -1)
    
    # Normaliza os vetores
    imagem1 = normalize(imagem1, axis=1)
    imagem2 = normalize(imagem2, axis=1)
    
    # Calcula a similaridade do cosseno
    similaridade = cosine_similarity(imagem1, imagem2)[0][0]
    return similaridade

def processar_imagens(pasta_origem, pasta_destino_similar, pasta_destino_processada):
    """
    Processa as imagens da pasta de origem, verifica similaridade e move para as pastas de destino.
    """
    imagens = [f for f in os.listdir(pasta_origem) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif', '.psd'))]
    imagem_base_path = os.path.join(pasta_origem, imagens[0])
    imagem_base = carregar_imagem(imagem_base_path)
    
    if imagem_base is None:
        print(f"Não foi possível carregar a imagem base {imagem_base_path}. Pulando...")
        return
    
    print(f"Iniciando o processamento das imagens a partir de {imagem_base_path}...")
    
    # Processamento das imagens
    for nome_imagem in imagens[1:]:
        imagem_path = os.path.join(pasta_origem, nome_imagem)
        
        # Verifica se a imagem é muito grande antes de carregá-la
        if not verificar_imagem_grande(imagem_path):
            continue
        
        imagem_atual = carregar_imagem(imagem_path)
        
        if imagem_atual is None:
            continue
        
        # Calcula a similaridade
        similaridade = calcular_similaridade(imagem_base, imagem_atual)
        
        if similaridade >= 0.75:
            # Se a similaridade for maior ou igual a 75%, move para pasta de imagens similares
            destino_similar = os.path.join(pasta_destino_similar, nome_imagem)
            shutil.move(imagem_path, destino_similar)
            print(f"Imagem {nome_imagem} movida para pasta de imagens similares.")
        else:
            # Se não for similar, move para a pasta de imagens processadas
            destino_processada = os.path.join(pasta_destino_processada, nome_imagem)
            shutil.move(imagem_path, destino_processada)
            print(f"Imagem {nome_imagem} movida para pasta de imagens processadas.")
    
    print("Processamento concluído.")

# Caminhos das pastas
pasta_origem = 'W:/1/ANEZIO PAINEIS 2021/tif'
pasta_destino_similar = 'W:/1/IMAGENS IGUAIS'
pasta_destino_processada = 'W:/1/IMAGENS PROCESSADAS'

# Chama a função de processamento
processar_imagens(pasta_origem, pasta_destino_similar, pasta_destino_processada)
