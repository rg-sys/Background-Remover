import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from rembg import remove
import os

# Function to select file from system
def upload_file():
    global filename
    f_types = [('Image Files', '*.jpg;*.jpeg;*.png')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    if filename:
        b2.config(state='normal')
        b1.config(state='disabled')

# Function to remove background of an image and then show message
def convert(image_name):
    try:
        current_working_directory = os.getcwd()
        input_path = filename
        output_path = os.path.join(current_working_directory, f'{image_name}.png')
        
        image_input = Image.open(input_path)
        output = remove(image_input)
        output.save(output_path)
        
        messagebox.showinfo('Success', 'Image background successfully removed')
        top.destroy()
    except Exception as e:
        messagebox.showerror('Error', f'An error occurred: {e}')

# Defining tkinter window
top = tk.Tk()
top.geometry("400x300")
top.title('Background Removal App')

my_font1 = ('times', 18, 'bold')

# Defining tkinter widgets and placing them using place
l1 = tk.Label(top, text='Background Removal App', font=my_font1)
l1.place(x=50, y=20)

b1 = tk.Button(top, text='Select Image', height=2, font=('Arial', 14), bg='green', fg='white', command=upload_file)
b1.place(x=125, y=70)

image_name = tk.StringVar()
image_name.set('enter file name')

e1 = tk.Entry(top, textvariable=image_name, font=('Arial', 14))
e1.place(x=50, y=150, width=300)

b2 = tk.Button(top, text='Convert Now', height=2, font=('Arial', 14), bg='green', fg='white', state='disabled', command=lambda: convert(image_name.get()))
b2.place(x=125, y=200)

top.mainloop()
