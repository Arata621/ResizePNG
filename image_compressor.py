import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import subprocess

def compress_images():
    file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.webp")])
    if not file_paths:
        return
    
    save_dir = filedialog.askdirectory()
    if not save_dir:
        return
    
    try:
        quality = int(quality_slider.get())
        for file_path in file_paths:
            image = Image.open(file_path)
            filename = os.path.basename(file_path)
            save_path = os.path.join(save_dir, filename)
            
            if file_path.lower().endswith(".png"):
                temp_path = save_path.replace(".png", "_temp.png")
                image.save(temp_path, optimize=True)
                subprocess.run(["pngquant", "--quality", f"{quality}-{quality+10}", "--output", save_path, temp_path], check=True)
                os.remove(temp_path)
            elif file_path.lower().endswith(('.jpg', '.jpeg')):
                image.save(save_path, optimize=True, quality=quality)
                subprocess.run(["jpegoptim", "--max=" + str(quality), save_path], check=True)
            else:
                image.save(save_path, optimize=True, quality=quality)
        
        messagebox.showinfo("Success", "Images compressed successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def drop_handler(event):
    file_paths = root.tk.splitlist(event.data)
    compress_images(file_paths)

# GUI Setup
root = tk.Tk()
root.title("Image Compressor")
root.geometry("400x250")
root.configure(bg="white")

tk.Label(root, text="Compression Level:").pack()
quality_slider = tk.Scale(root, from_=10, to=100, orient="horizontal")
quality_slider.set(75)
quality_slider.pack()

tk.Button(root, text="Select Images & Compress", command=compress_images).pack(pady=10)

root.mainloop()
