import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread("4634081-middle.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir intervalo de cores para o fundo
lower_bound = np.array([0, 0, 200])  # Ajuste os valores
upper_bound = np.array([180, 20, 255])

# Criar máscara
mask = cv2.inRange(hsv, lower_bound, upper_bound)
mask_inv = cv2.bitwise_not(mask)

# Aplicar a máscara
result = cv2.bitwise_and(image, image, mask=mask_inv)
cv2.imwrite("imagem_sem_fundo.png", result)
