from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import argparse

def obtener_decimal_from_obj(info, referencia):
    grados = float(info[0])
    minutos = float(info[1])
    segundos = float(info[2])
    
    decimal = grados + (minutos / 60.0) + (segundos / 3600.0)
    if referencia in ['S', 'W']:
        decimal = -decimal
    return decimal

def extraer_info_completa(ruta_imagen):
    try:
        imagen = Image.open(ruta_imagen)
        exif_data = imagen._getexif()
        
        if not exif_data:
            print("No se encontraron metadatos EXIF en esta imagen.")
            return

        print(f"{'INFORMACIÓN DE LA CÁMARA':^50}")
        info_gps = {}
        
        for tag_id, valor in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            
            if tag == 'GPSInfo':
                for key in valor:
                    sub_tag = GPSTAGS.get(key, key)
                    info_gps[sub_tag] = valor[key]
            else:
                if tag in ['Make', 'Model', 'ExposureTime', 'FNumber', 'ISOSpeedRatings', 'DateTime']:
                    print(f"{tag:20}: {valor}")

        print(f"\n{'Coordenadas GPS':^50}")
        if 'GPSLatitude' in info_gps and 'GPSLongitude' in info_gps:
            lat = obtener_decimal_from_obj(info_gps['GPSLatitude'], info_gps['GPSLatitudeRef'])
            lon = obtener_decimal_from_obj(info_gps['GPSLongitude'], info_gps['GPSLongitudeRef'])
            
            print(f"Latitud: {lat}")
            print(f"Longitud: {lon}")
            print(f"Google Maps: https://www.google.com/maps?q={lat},{lon}")
        else:
            print("La imagen no contiene coordenadas GPS.")

    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

parser = argparse.ArgumentParser()
parser.add_argument("--url", required=True, type=str)

args = parser.parse_args()

extraer_info_completa(args.url)