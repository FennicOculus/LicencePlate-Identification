import tkinter as tk
from PIL import ImageTk, Image
from OneCar import reco
from PlateExtraction import addCar


    
win = tk.Tk()
win.title('Parking Plate Identification')
win.geometry("640x480")
win.resizable(0,0)

frame = tk.Frame(win, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
img = Image.open("Interface/BackGround.jpg")
img = ImageTk.PhotoImage(img.resize((640, 480)))

label = tk.Label(frame, image = img)
label.pack()


button1 = tk.Button(win, text='Recognition From Image', width=25, command=reco)
button1.pack(side='left', padx=50, pady=0)

button2 = tk.Button(win, text='Add Car To Database', width=25, command=addCar)
button2.pack(side='right', padx=50, pady=0)



win.mainloop()
win.quit()

