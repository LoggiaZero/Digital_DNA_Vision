import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

def edge_filter(path):
    img = cv2.imread(path, 0)
    
    edges = cv2.Canny(img, 100, 200)

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(np.abs(fshift))

    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Imagen Original (Grises)')

    plt.subplot(1, 3, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Filtro Canny (Bordes)')

    plt.subplot(1, 3, 3)
    plt.imshow(magnitude_spectrum, cmap='jet')
    plt.title('Espectro de Fourier (Frecuencias)')
    
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, type=str)

args = parser.parse_args()

edge_filter(args.url)