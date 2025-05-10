import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import stepic
import os

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ashka Stego App 💕")
        self.root.geometry("500x600")
        self.root.configure(bg="#ffe6f0")

        self.image_path = None

        tk.Label(root, text="Secret Message 💌", bg="#ffe6f0", fg="#d63384", font=("Arial", 14)).pack(pady=10)
        self.message_entry = tk.Text(root, height=5, width=40, font=("Arial", 12))
        self.message_entry.pack(pady=5)

        tk.Button(root, text="📁 Upload Image", command=self.upload_image, bg="#d63384", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(root, text="🔐 Encode Message", command=self.encode_message, bg="#28a745", fg="white", font=("Arial", 12)).pack(pady=10)
        tk.Button(root, text="🔓 Decode Message", command=self.decode_message, bg="#17a2b8", fg="white", font=("Arial", 12)).pack(pady=10)

    def upload_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("PNG Images", "*.png")])
        if self.image_path:
            messagebox.showinfo("Image Selected", f"Selected: {os.path.basename(self.image_path)}")

    def encode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Upload an image first!")
            return
        msg = self.message_entry.get("1.0", tk.END).strip()
        if not msg:
            messagebox.showerror("Error", "Enter a secret message!")
            return

        img = Image.open(self.image_path)
        encoded_img = stepic.encode(img, msg.encode())
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            encoded_img.save(save_path)
            messagebox.showinfo("Success", f"Message hidden in image!\nSaved to: {save_path}")

    def decode_message(self):
        if not self.image_path:
            messagebox.showerror("Error", "Upload an image first!")
            return
        img = Image.open(self.image_path)
        try:
            msg = stepic.decode(img)
            self.message_entry.delete("1.0", tk.END)
            self.message_entry.insert(tk.END, msg)
            messagebox.showinfo("Decoded Message", msg)
        except Exception as e:
            messagebox.showerror("Error", f"Couldn't decode message.\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()
