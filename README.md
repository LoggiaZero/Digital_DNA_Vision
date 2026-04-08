# Digital DNA Vision

## Context
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