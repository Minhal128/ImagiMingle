import requests
import io
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from ttkbootstrap import Style

root = tk.Tk()
root.title("Image Generator")
root.geometry("700x600")
root.config(bg="grey")
root.resizable(False, False)
style = Style(theme="sandstone")    

style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('like.TButton', foreground='green', background='white')
style.configure('unlike.TButton', foreground='red', background='white')
style.configure('download.TButton', foreground='blue', background='white')

current_image_data = None
current_image_url = None

def display_image(category):
    global current_image_data, current_image_url
    
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=Gb78V27Jp6lime1lAKzYaJW_sUOn8Zh5ujWc0lbjF7o&w=3840&h=2160"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        current_image_url = data["urls"]["raw"]  

        img_data = requests.get(current_image_url).content  

        photo = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)).resize((600, 400), resample=Image.LANCZOS))
        label.config(image=photo)
        label.image = photo
        like_button.config(state="normal")
        unlike_button.config(state="normal")
        download_button.config(state="normal")

        current_image_data = img_data  
    except requests.exceptions.RequestException as e:
        print(f"Error requesting data from Unsplash API: {e}")

def enable_button(*args):
    generate_button.config(state="normal" if category_var.get() != "Choose Category" else "disabled")

def like_image():
    print("Image liked!")

def unlike_image():
    print("Image unliked!")

def download_image():
    global current_image_url, current_image_data
    
    if current_image_url and current_image_data:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'wb') as file:
                    file.write(current_image_data)
                print(f"Image saved to {file_path}")
            except IOError as e:
                print(f"Error saving image: {e}")

def start_generation():
    display_image(category_var.get())

def exit_program():
    root.destroy()

def create_gui():
    global category_var, generate_button, label, like_button, unlike_button, download_button

    category_var = tk.StringVar(value="Choose Category")
    category_options = ["Choose Category", "Food", "Animals", "People", "Marvel", "Art", "Technology", "Vehicles", "Moon", "Sky", "love", "Aesthetic", "Babies", "Random"]
    category_dropdown = ttk.OptionMenu(root, category_var, *category_options, command=enable_button)
    category_dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    category_dropdown.config(width=14)

    generate_button = ttk.Button(text="Generate Image", state="disabled", command=start_generation)
    generate_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    label = tk.Label(root, background="white")
    label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    like_button = ttk.Button(root, text="Like", state="disabled", command=like_image, style="like.TButton")
    like_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    unlike_button = ttk.Button(root, text="Unlike", state="disabled", command=unlike_image, style="unlike.TButton")
    unlike_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
    
    download_button = ttk.Button(root, text="Download", state="disabled", command=download_image, style="download.TButton")
    download_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    
    start_button = ttk.Button(root, text="Start", command=start_generation)
    start_button.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")
    
    exit_button = ttk.Button(root, text="Exit", command=exit_program)
    exit_button.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

    root.columnconfigure([0, 1], weight=1)
    root.rowconfigure(1, weight=1)
    root.mainloop()

if __name__ == '__main__':
    create_gui()
