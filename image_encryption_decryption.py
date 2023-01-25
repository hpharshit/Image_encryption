# Image Encryption Decryption

# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import os
import numpy as np
from cv2 import *
import random


def AES():
    img = "#$%^@@"
    return img

def encrypt_image(image_path, key):
    # Open the image file
    with Image.open(image_path) as im:
        # Convert the image to bytes
        #image_bytes = io.BytesIO()
        im.save(image_bytes, format='PNG')
        image_bytes = image_bytes.getvalue()

    # Generate a random initialization vector
    iv = os.urandom(16)

    # Create a new AES cipher
    #cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the image bytes to a multiple of 16
    padded_image_bytes = image_bytes + b' ' * (16 - (len(image_bytes) % 16))

    # Encrypt the padded image bytes
    encrypted_image_bytes = AES(padded_image_bytes)

    # Return the initialization vector and the encrypted image bytes
    return iv, encrypted_image_bytes


#created main window
window = Tk()
window.geometry("1920x1080")
window.title("Image Encryption Decryption")

window.configure(bg='azure4')

# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
'''C = Canvas(window, bg="blue", height=2500, width=3000)
filename = PhotoImage(file = "cn44.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

C.pack()'''

# defined variable
global count, emig
# global bright, con
# global frp, tname  # list of paths
frp = []
tname = []
con = 1
bright = 0
panelB = None
panelA = None

# function defined to get the path of the image selected
def getpath(path):
    a = path.split(r'/')
    # print(a)
    fname = a[-1]
    l = len(fname)
    location = path[:-l]
    return location

# function defined to get the folder name from which image is selected
def getfoldername(path):
    a = path.split(r'/')
    # print(a)
    name = a[-1]
    return name
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con



# function defined to get the file name of image is selected
def getfilename(path):
    a = path.split(r'/')
    fname = a[-1]
    a = fname.split('.')
    a = a[0]
    return a

# function defined to open the image file
def openfilename():
    filename = filedialog.askopenfilename(title='"pen')
    return filename

# function defined to open the selected image
def open_img():
    global x, panelA, panelB
    global count, eimg, location, filename
    count = 0
    x = openfilename()
    img = Image.open(x)
    eimg = img
    img = ImageTk.PhotoImage(img)
    temp = x
    location = getpath(temp)
    filename = getfilename(temp)
    # print(x)
    if panelA is None or panelB is None:
        panelA = Label(image=img)
        panelA.image = img
        panelA.pack(side="left", padx=10, pady=10)
        panelB = Label(image=img)
        panelB.image = img
        panelB.pack(side="right", padx=10, pady=10)
    else:
        panelA.configure(image=img)
        panelB.configure(image=img)
        panelA.image = img
        panelB.image = img

# function defined for make the sketch of image selected
def en_fun():
    global x, image_encrypted, key
    # print(x)
    image_input = cv2.imread(x, 0)# 'C:/Users/aakas/Documents/flower.jpg'
    (x1, y) = image_input.shape
    image_input = image_input.astype(float) / 255.0
    # print(image_input)

    mu, sigma = 0, 0.1  # mean and standard deviation
    key = np.random.normal(mu, sigma, (x1, y)) + np.finfo(float).eps
    # print(key)
    image_encrypted = image_input / key
    cv2.imwrite('image_encrypted.jpg', image_encrypted * 255)

    imge = Image.open('image_encrypted.jpg')
    imge = ImageTk.PhotoImage(imge)
    panelB.configure(image=imge)
    panelB.image = imge
    mbox.showinfo("Encrypt Status", "Image Encryted successfully.")

# function defined to make the image sharp
def de_fun():
    global image_encrypted, key
    image_output = image_encrypted * key
    image_output *= 255.0
    cv2.imwrite('image_output.jpg', image_output)

    imgd = Image.open('image_output.jpg')
    imgd = ImageTk.PhotoImage(imgd)
    panelB.configure(image=imgd)
    panelB.image = imgd
    mbox.showinfo("Decrypt Status", "Image decrypted successfully.")

# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
# function defined to reset the edited image to original one
def reset():
    # print(x)
    image = cv2.imread(x)[:, :, ::-1]
    global count, eimg
    count = 6
    global o6
    o6 = image
    image = Image.fromarray(o6)
    eimg = image
    image = ImageTk.PhotoImage(image)
    panelB.configure(image=image)
    panelB.image = image
    mbox.showinfo("Success", "Image reset to original format!")

# function defined to same the edited image
def save_img():
    global location, filename, eimg
    print(filename)
    # eimg.save(location + filename + r"_edit.png")
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    eimg.save(filename)
    mbox.showinfo("Success", "Encrypted Image Saved Successfully!")


# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
## global bright, con
# global frp, tname  # list of paths global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con

# top label
start1 = tk.Label(text = "Image Encryption Decryption", font=("Times New Roman Bold", 40), fg="black", bg="azure4") # same way bg
start1.place(x = 430, y = 10)

# original image label
start1 = tk.Label(text = "Original Image", font=("Times New Roman Bold", 20), fg="red", bg="azure4") # same way bg
start1.place(x = 200, y = 630)

# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
# edited image label
start1 = tk.Label(text = "Encrypted/Decrypted Image", font=("Times New Roman Bold", 20), fg="green", bg="azure4") # same way bg
start1.place(x = 1060, y = 630)

# choose button created
chooseb = Button(window, text="Choose",command=open_img,font=("Franklin Gothic Heavy", 15), bg = "green", fg = "white", borderwidth=3, relief="raised")
chooseb.place(x =30 , y =20 )

# save button created
saveb = Button(window, text="Save",command=save_img,font=("Franklin Gothic Heavy", 15), bg = "black", fg = "white", borderwidth=3, relief="raised")
saveb.place(x =170 , y =20 )

# Encrypt button created
enb = Button(window, text="Encrypt",command=en_fun,font=("Franklin Gothic Heavy", 15), bg = "red", fg = "white", borderwidth=3, relief="raised")
enb.place(x =50 , y =700)

# decrypt button created
deb = Button(window, text="Decrypt",command=de_fun,font=("Franklin Gothic Heavy", 15), bg = "green", fg = "white", borderwidth=3, relief="raised")
deb.place(x =725 , y =700 )


# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
# reset button created
resetb = Button(window, text="Reset",command=reset,font=("Franklin Gothic Heavy", 15), bg = "blue", fg = "white", borderwidth=3, relief="raised")
resetb.place(x =1300, y =700)

# function created for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# exit button created
exitb = Button(window, text="EXIT",command=exit_win,font=("Franklin Gothic Heavy", 15), bg = "red", fg = "white", borderwidth=3, relief="raised")
exitb.place(x =1300, y =20 )


window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths
    # global bright, con
# global frp, tname  # list of paths