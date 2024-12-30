from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Gallery")
root.iconbitmap(r"C:\Users\rahul  sah\Desktop\pycharm")

my_img = ImageTk.PhotoImage(Image.open(r"C:\Users\rahul  sah\Desktop\pycharm\ji.png.png"))
my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\rahul  sah\Desktop\pycharm\gi.png.png"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\rahul  sah\Desktop\pycharm\pi.png.png"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\rahul  sah\Desktop\pycharm\bi.png.png"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\rahul  sah\Desktop\pycharm\oi.png.png"))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4]

image_index = 0

status = Label(root, text=" image 1 of " + str(len(image_list)), bd=1, relief="sunken")

my_label = Label(image=image_list[image_index])
my_label.grid(row=0, column=0, columnspan=3)

def forward():
    global image_index, my_label
    image_index += 1
    if image_index == len(image_list):
        image_index = 0
    my_label.grid_forget()
    my_label = Label(image=image_list[image_index])
    my_label.grid(row=0, column=0, columnspan=3)

    if image_index == len(image_list) - 1:
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)

    if image_index == 0:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    status = Label(root, text=" image " + str(image_index+1) + " of " + str(len(image_list)), bd=1, relief="sunken")
    status.grid(row=2, column=0, columnspan=3)

def back():
    global image_index, my_label
    image_index -= 1
    if image_index < 0:
        image_index = len(image_list) - 1
    my_label.grid_forget()
    my_label = Label(image=image_list[image_index])
    my_label.grid(row=0, column=0, columnspan=3)

    if image_index == len(image_list) - 1:
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)

    if image_index == 0:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)

    status = Label(root, text=" image " + str(image_index+1) + " of " + str(len(image_list)), bd=1, relief="sunken")
    status.grid(row=2, column=0, columnspan=3)

    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

button_back = Button(root, text="<<", command=back)
button_forward = Button(root, text=">>", command=forward)

quit1 = Button(root, text="Exit", command=root.quit)
quit1.grid(row=1, column=1, pady=15, padx=15)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3)
