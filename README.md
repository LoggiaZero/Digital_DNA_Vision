# Digital DNA Vision

**Digital DNA Vision** is a forensic toolkit designed to detect digital image alterations by analyzing "digital DNA"—the metadata and pixel-level patterns left after manipulation. Developed in a strategic partnership between **Corporativo LZ** and **FICA-UJED** (Facultad de Ingeniería, Ciencias y Arquitectura, Universidad Juárez del Estado de Durango).

---

## Table of Contents

- [Features](#features)
- [Technical Overview](#technical-overview)
- [Installation](#installation)
- [Usage](#usage)
  - [Metadata Extraction (`meta_img.py`)](#metadata-extraction-meta_imgpy)
- [Project Specifications](#project-specifications)
- [Contact](#contact)
- [License](#license)

---

## Features

- **Metadata Analysis:** Extract hidden EXIF and file properties
- **Color Channel Decomposition:** Analyze color space distributions
- **Structural Filtering:** Detect image border and edge anomalies
- **Frequency Spectrum Analysis:** Reveal resampling/synthetic noise
- **Data Visualization:** Produce forensic reports and visual summaries

---

## Technical Overview

- **Language:** Python (100%)
- **Environment:** Python 3.x, virtual environment (`venv`)
- Uses:
  - `Pillow` for extracting EXIF metadata
  - `OpenCV` for color spaces and edge filtering
  - `Matplotlib` for visualizations
  - FFT libraries for frequency domain analysis

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LoggiaZero/Digital_DNA_Vision.git
   cd Digital_DNA_Vision
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, ensure you install:
   ```
   pip install pillow opencv-python matplotlib
   ```

---

## Usage

### Metadata Extraction (`meta_img.py`)

This script is responsible for the initial forensic layer: **Metadata Extraction**. It parses the image file to extract embedded EXIF information that can help identify the source device and capture conditions.

- **Extracted Data:**
  - Device information (brand, model)
  - Camera parameters (aperture, shutter speed, ISO, focal length)
  - Geospatial data (GPS, location timestamps)

If no EXIF headers are present, it will output:
```
No EXIF metadata was found in this file
```

**Command:**
```bash
python meta_img.py --url image_path
```

![Respuesta de una imagen con metadatos](/assets/meta_img_1.png "Respuesta de una imagen con metadatos")
![Respuesta de una imagen sin metadatos](/assets/meta_img_2.png "Respuesta de una imagen sin metadatos")