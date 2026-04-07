import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

def robert(path_imagen):
    try:
        img = cv2.imread(path_imagen, cv2.IMREAD_GRAYSCALE)
        if img is None: raise FileNotFoundError

        kernel_roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)

        kernel_roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)

        roberts_x = cv2.filter2D(img, cv2.CV_32F, kernel_roberts_x)
        roberts_y = cv2.filter2D(img, cv2.CV_32F, kernel_roberts_y)

        roberts_magnitude = cv2.magnitude(roberts_x, roberts_y)
        
        roberts_edges = cv2.normalize(roberts_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

        plt.figure(figsize=(12, 6))
        
        plt.subplot(1, 2, 1)
        plt.imshow(img, cmap='gray')
        plt.title('Imagen Original (Grises)')
        plt.axis('off')

        plt.subplot(1, 2, 2)
        plt.imshow(roberts_edges, cmap='magma') 
        plt.title('Bordes Roberts (Sensibilidad a Alta Frecuencia)')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        print("Error: No se pudo encontrar o leer la imagen.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, type=str)

args = parser.parse_args()

robert(args.url)