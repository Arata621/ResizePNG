![Squirreless Banner](https://raw.githubusercontent.com/Arata621/Squirreless/main/Config/banner.png)

# squirreless.py

A **cross-platform** image compression tool that supports **PNG, JPG, JPEG, and WebP**. Allows you to manually adjust compression levels and supports **batch processing** & **drag-and-drop functionality**. Works **100% offline**!

---

## ⚠️ Warning
For Windows users, I recommend using **v1.0.0** because for this specific OS, **1.1.0** is unstable and sometimes will not give expected results. For macOS and Linux users, please use **v1.1.0** because in this case, **1.1.0** is more stable and has better compression rates. For setting up **v1.0.0**, use the "deprecated" version of the README and Python code. For setting up **v1.1.0**, use the *latest version* of the README and Python code.

---

## Features
✅ **Compress PNG, JPG, JPEG, and WebP files** with **high compression levels**  
✅ **Batch compression** (Select & compress multiple images at once)  
✅ **Drag & Drop support** (Simply drag images into the app)  
✅ **Manual compression level adjustment** via a slider  
✅ **Uses `pngquant` (for PNGs) and `jpegoptim` (for JPGs) for superior compression**  
✅ **Works offline** (No internet required)  
✅ **Cross-platform** (Windows, macOS, Linux)  

---

## 🛠 Installation Guide

### **1️⃣ Install Python** (Skip if already installed)

#### Windows:
1. Download **Python 3** from [python.org](https://www.python.org/downloads/windows/).
2. Install it **and check** `Add Python to PATH` **during installation**.
3. Open **Command Prompt (cmd)** and run:
   ```bash
   python --version
   ```
   If you see `Python 3.x.x`, you’re good! ✅

#### macOS:
1. Open **Terminal** (`Cmd + Space` → Search "Terminal").
2. Run:
   ```bash
   python3 --version
   ```
   If Python isn’t installed, install it using Homebrew:
   ```bash
   brew install python
   ```

#### Linux (Ubuntu/Debian):
1. Open **Terminal** and run:
   ```bash
   sudo apt update && sudo apt install python3
   ```
2. Verify installation:
   ```bash
   python3 --version
   ```

---

### **2️⃣ Install Required Dependencies**
Run the following command:
```bash
pip install pillow
```
> If that doesn’t work, try:
```bash
pip3 install pillow
```

#### **(Required for Better Compression)** Install `pngquant` and `jpegoptim`

✅ **Windows:**
- Download [pngquant](https://pngquant.org/) and [jpegoptim (Windows version)](https://github.com/imagemin/jpegoptim-bin)
- Add them to your system **PATH**

✅ **macOS (via Homebrew):**
```bash
brew install pngquant jpegoptim
```
✅ **Linux (Ubuntu/Debian):**
```bash
sudo apt install pngquant jpegoptim
```

---

### **3️⃣ Run the Compressor**
1. **Download the script** & save it as `image_compressor.py`
2. Open **Terminal / Command Prompt**
3. Navigate to the script's folder:
   - **Windows**:
     ```bash
     cd C:\path\to\your\script
     ```
   - **macOS/Linux**:
     ```bash
     cd /path/to/your/script
     ```
4. **Run the script**:
   - **Windows**:
     ```bash
     python image_compressor.py
     ```
   - **macOS/Linux**:
     ```bash
     python3 image_compressor.py
     ```

🎉 **The Image Compressor UI will open!**
- Click **"Select Images & Compress"**
- Choose multiple PNG/JPG/WebP files
- Adjust the **slider** for compression level
- **Compressed images will be saved in your chosen folder!**

---

### **(Optional) Convert to an Executable**
If you want to **turn this into a standalone app** (so you don’t need to run Python manually), follow these steps:

#### **Windows (.exe)**
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Convert script to an executable:
   ```bash
   pyinstaller --onefile --windowed image_compressor.py
   ```
3. Your `.exe` file will be in the `dist/` folder.

#### **macOS/Linux (Executable)**
1. Install PyInstaller:
   ```bash
   pip3 install pyinstaller
   ```
2. Run:
   ```bash
   pyinstaller --onefile --windowed image_compressor.py
   ```
3. The executable will be in the `dist/` folder.

## Attributions
---
The banner icon used in this project was designed by [Freepik](https://www.freepik.com).
