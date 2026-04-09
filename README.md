# Digital DNA Vision

**Digital DNA Vision** is a collaborative forensic tool developed through a strategic partnership between **Corporativo LZ** and **FICA-UJED** (Facultad de Ingeniería, Ciencias y Arquitectura de la Universidad Juárez del Estado de Durango). Based in **Gómez Palacio, Durango**, this project unites industrial expertise with academic research to address the challenges of digital authenticity.

The repository is designed to detect digital alterations in images by analyzing their "digital DNA"—the underlying metadata and pixel-level patterns that remain after manipulation.

### Technical Overview
The project is implemented in **Python** and operates within a dedicated virtual environment (`venv`). It leverages a specialized stack of libraries to perform five fundamental forensic functions:

* **Metadata Analysis:** Uses `Pillow` to extract hidden EXIF data and file properties.
* **Channel Decomposition:** Uses `OpenCV` to split RGB channels and analyze color space distributions.
* **Structural Filtering:** Applies border and edge detection filters via `OpenCV` to find anomalies in image composition.
* **Frequency Domain Inspection:** Computes the **Fourier Transform** to analyze the frequency spectrum for signs of resampling or synthetic noise.
* **Data Visualization:** Utilizes `Matplotlib` to generate forensic reports and visual representations of the processed data.

### Project Specifications
* **Location:** Gómez Palacio, Durango, México
* **License:** [MIT](https://choosealicense.com/licenses/mit/)
* **Environment:** Python `venv`
* **Partners:** Corporativo LZ & FICA-UJED

---

### Contact Information
**Ph.D. José Armando Sáenz Esqueda** 
* **Corporate Email:** [jsaenz@loggiazero.com.mx](mailto:jsaenz@loggiazero.com.mx)  
* **Academic Email:** [jsaenz@ujed.mx](mailto:jsaenz@ujed.mx)  
* **LinkedIn:** [linkedin.com/in/armandosaenz/](https://www.linkedin.com/in/armandosaenz/)

---

## Documentation: meta_img.py

This script is responsible for the initial forensic layer: **Metadata Extraction**. It parses the image file to retrieve embedded information that can identify the source device and the conditions under which the image was captured.

### Description
The script extracts EXIF (Exchangeable Image File Format) data, specifically targeting:
* **Device Information:** Cellphone brand and model.
* **Camera Parameters:** Aperture, shutter speed, ISO, and focal length.
* **Geospatial Data:** GPS coordinates and location timestamps.

If the file has been stripped of its metadata or was created in a way that does not generate EXIF headers, the script will return:  
`No EXIF metadata was found in this file`

### Syntax
To run the analysis, use the following command in your terminal:

```bash
python meta_img.py --url image_path
```

### Examples

![Output for an image with metadata](/assets/meta_img_1.png)
*Figure 1: Output for an image with metadata*

![Output for an image without metadata](/assets/meta_img_2.png)
*Figure 2: Output for an image without metadata*

## Documentation: SplitRGB.py

This script performs **Chromatic Decomposition**, allowing for a detailed inspection of the individual color channels. This is essential in forensic analysis to detect inconsistencies in noise distribution or localized color manipulation that may not be visible in the full-color composite.

### Description
The script processes the input image and generates a single visualization window containing a 1x4 grid:
1. **Original Image:** The source file in full color.
2. **Red Channel:** Grayscale intensity map of the red spectrum.
3. **Green Channel:** Grayscale intensity map of the green spectrum.
4. **Blue Channel:** Grayscale intensity map of the blue spectrum.

### Syntax
Run the following command in your terminal:

```bash
python SplitRGB.py --url image_path
```

### Example

![Expected output for SplitRGB.py](/assets/meta_img_1.png)
*Figure 3: Expected output for SplitRGB.py*

