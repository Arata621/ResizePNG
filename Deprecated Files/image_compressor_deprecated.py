import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

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
quality_slider = tk.Scale(root, from_=1, to=100, orient="horizontal")
quality_slider.set(75)
quality_slider.pack()

tk.Button(root, text="Select Images & Compress", command=compress_images).pack(pady=10)

root.mainloop()
