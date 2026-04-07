import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse 

def analizar_imagen(path):
    img = cv2.imread(path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    R, G, B = cv2.split(img_rgb)

    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 4, 1)
    plt.imshow(img_rgb)
    plt.title("Original (RGB)")
    
    plt.subplot(1, 4, 2)
    plt.imshow(R, cmap='Reds')
    plt.title("Canal Rojo (R)")
    
    plt.subplot(1, 4, 3)
    plt.imshow(G, cmap='Greens')
    plt.title("Canal Verde (G)")
    
    plt.subplot(1, 4, 4)
    plt.imshow(B, cmap='Blues')
    plt.title("Canal Azul (B)")
    
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, type=str)

args = parser.parse_args()

analizar_imagen(args.url)