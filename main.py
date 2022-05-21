import tkinter as tk
from PIL import ImageTk, Image
from OneCar import reco
from PlateDetection import Seg
from PlateExtraction import addCar
from CameraDetection import vidRec

win = tk.Tk()
win.title('Parking Plate Identification')
win.geometry("760x560")
win.resizable(0,0)

frame = tk.Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = Image.open("Interface/BackGround.jpg")
img = ImageTk.PhotoImage(img.resize((770, 570)))

label = tk.Label(frame, image = img)
label.pack()


button1 = tk.Button(win, text='Recognition From Image', width=25, command=reco)
button1.pack(side='left', padx=50, pady=0)

button2 = tk.Button(win, text='Manually Adding Car To Database', width=25, command=addCar)
button2.pack(side='right', padx=50, pady=0)

button3 = tk.Button(win, text='Ajout Automatique Matricule', width=25, command=Seg)
button3.pack(side='top', padx=0, pady=150)

button3 = tk.Button(win, text='Ouvrir Caméra', width=25, command=vidRec)
button3.pack(side='bottom', padx=0, pady=100)



win.mainloop()
win.quit()

