import pyqrcode
import png
from tkinter import *

def get_code():
    data_var = data.get()
    qr = pyqrcode.create(str(data_var))
    qr.png('Qrcode.png', scale=6)

base = Tk()
base.geometry("500x200")
base.title("QRCode Generator")

data = StringVar()

dataEntry = Entry(textvariable=data, width="55")
dataEntry.place(x=80,y=50)

button = Button(base,text="Get your Code",command=get_code,width="30",height="2",bg="grey")
button.place(x=150,y=100)

base.mainloop()
