import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

def advanced_analytics(path1, path2):
    rutas = [path1, path2]
    titulos = ["Imagen A (Real)", "Imagen B (Sugerida IA)"]
    
    plt.figure(figsize=(16, 10))

    for i, path in enumerate(rutas):
        # 1. Carga y preprocesamiento
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Error: No se pudo cargar {path}")
            continue

        canny = cv2.Canny(img, 100, 200)

        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

        plt.subplot(2, 3, i*3 + 1)
        plt.imshow(img, cmap='gray')
        plt.title(f"{titulos[i]} - Original")
        plt.axis('off')

        plt.subplot(2, 3, i*3 + 2)
        plt.imshow(canny, cmap='gray')
        plt.title(f"Bordes (Canny)")
        plt.axis('off')

        plt.subplot(2, 3, i*3 + 3)
        plt.imshow(magnitude_spectrum, cmap='jet')
        plt.title(f"Espectro (Fourier)")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("--url1", required=True, type=str)
parser.add_argument("--url2", required=True, type=str)

args = parser.parse_args()

advanced_analytics(args.url1, args.url2)