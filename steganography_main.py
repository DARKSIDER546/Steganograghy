from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetype=(("PNG file", "*.png"),
                                                    ("JPG File", "*.jpg"), ("All file", "*.txt")))
    
    if filename:
        img = Image.open(filename)
        
        
        img_width, img_height = img.size
        
        
        max_width, max_height = 250, 250  
        
        
        if img_width > max_width or img_height > max_height:
            
            ratio = min(max_width / img_width, max_height / img_height)
            new_width = int(img_width * ratio)
            new_height = int(img_height * ratio)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)  

        
        img = ImageTk.PhotoImage(img)
        
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

def Hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message)

def Show():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def save():
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"),
                                                        ("JPG files", "*.jpg")],
                                             title="Save Image As")
    if file_path:
        secret.save(file_path)

image_icon=PhotoImage(file="C:\Users\Lenovo\Desktop\pythonPRO\logo.jpg.jpg")
root.iconphoto(False,image_icon)

logo=PhotoImage(file="C:/Users/Arghyanil/Desktop/Python Projects/logo.png")
Label(root,image=logo,bg="#2f4155").place(x=10,y=0)

Label(root, text="STEGANOGRAPHY USING PYTHON",bg="#2d4155",fg="white",font="arial 25 bold").place(x=100,y=20)

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1=Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

frame3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font="arial 14 bold",command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font="arial 14 bold",command=save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

frame4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font="arial 14 bold",command=Hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font="arial 14 bold",command=Show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()
