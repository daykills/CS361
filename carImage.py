import tkinter as tk
from PIL import Image,ImageTk,ImageFilter
import json
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import*

import tkinter as tk
from tkinter import filedialog

try:
    from PIL import Image     
except ImportError:
    import Image

import requests
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt


gui = tk.Tk()
gui.title("Car Photoshop Showcase")  
gui.geometry("900x500")
gui.configure(background = 'lightsteelblue') 

####### user input area#############
userTextEntry = tk.Entry(gui, bg = 'white', font = ("Monaco", 15))
userTextEntry.place(x = 13, y = 55, height = 70, width = 370)
userTextLabel = tk.Label(gui, text = "User Input from Scraper's UI ", bg = "lightsteelblue", bd = 10, fg = "black", font = ("Monaco", 20)) 
userTextLabel.place(x = 20, y = 3)

def sumbitBtn():
  # get scrapper's user input and disput
  try:
    f = open('kevin/CS361-Project/car.json')
    data = json.load(f)    
    carBrand = data["brand"]
    print(carBrand)
    userTextEntry.insert(END, carBrand)
    f.close()
  except FileNotFoundError:
      tk.messagebox.showinfo('user input is missing!')

optionButton = tk.Button(gui, text="Sumbit", command=sumbitBtn)
optionButton.place(x = 140, y = 160, width = 100)


###### #use teammate's output #############

entryLeft = tk.Entry(gui,borderwidth = 3, background = "darkgrey")
entryLeft.place(x = 10, y = 250, width = 380, height = 200)

textEntryLabel = tk.Label(gui, text = "Double Click to Select Art Affect ", bg = "lightsteelblue", bd = 10, fg = "black", font = ("Monaco", 20)) 
textEntryLabel.place(x = 450, y = 3)


def callJson():
  try:
    f = open('kevin/CS361-Project/car.json')
    data = json.load(f)    
    temp = data["img"]
    url = temp
    response = requests.get(url,stream=True)
    img = Image.open(response.raw)
    img.save("pic/origin.jpg")
    f.close()
  except FileNotFoundError:
      tk.messagebox.showinfo('user input is missing!')

    
#use teammate's output
def displayfunction():
    #resize the original pic
    callJson()
    global img
    temp = Image.open("pic/origin.jpg")
    outputFile = temp.resize((360,200),Image.ANTIALIAS)
    outputFile.save("pic/display.jpg")
    #add resized pic to canvas
    img= ImageTk.PhotoImage(Image.open("pic/display.jpg"))
    label_img = tk.Label(entryLeft, image = img)
    label_img.pack()
    

#create a display button for user to click
displayButton = tk.Button(height = 1, width = 2, command = displayfunction, text = "display")
displayButton.place(x = 160, y = 460, width = 60, height = 30)

#create a label of button 
displayButtonLabel = tk.Label(gui, text = "User Click to Display Orginal Image ", bg = "lightsteelblue", fg = "black", font = ("Monaco", 15)) 
displayButtonLabel.place(x = 20, y = 220)


#####add listbox ###########"
playList =    [ "CONTOUR",
                "EMBOSS",
                "EDGE_ENHANCE_MORE",
                "BLUR",
                "DETAIL",
                "FIND_EDGES",
                "EDGE_ENHANCE",
                "SMOOTH_MORE",
                "SMOOTH",
                "SHARPEN",
                "RankFilter",
                "MaxFilter",
                "MinFilter",
                ]
playList_dict = {"CONTOUR": ImageFilter.CONTOUR,
                  "EMBOSS": ImageFilter.EMBOSS,
                  "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
                  "BLUR": ImageFilter.BLUR,
                  "DETAIL": ImageFilter.DETAIL,
                  "FIND_EDGES":ImageFilter.FIND_EDGES,
                  "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
                  "SMOOTH_MORE": ImageFilter.SMOOTH_MORE,
                  "SMOOTH": ImageFilter.SMOOTH,
                  "SHARPEN": ImageFilter.SHARPEN,
                  "RankFilter": ImageFilter.RankFilter(5,0),
                  "MaxFilter": ImageFilter.MaxFilter(3),
                  "MinFilter":  ImageFilter.MinFilter(3),
                }
def CurSelet(self):
    key = str((listbox.get(ACTIVE)))
    print(key)
    print(playList_dict[key])
    temp = Image.open("pic/display.jpg")
    new_img = temp.filter(playList_dict[key])
    new_img.save("new_img.jpg")
    outputFile = new_img.resize((1000,600),Image.ANTIALIAS)
    outputFile.save("pic/{}.jpg".format(key))


listbox = tk.Listbox(gui, background="Blue", fg="white",selectbackground="Red",highlightcolor="Red")
listbox.bind('<<ListboxSelect>>',CurSelet)
listbox.place(x=455, y=60,height = 140, width = 360)

for x in playList:
    listbox.insert(END, x)

###### user click modify button #############
entryRight = tk.Entry(gui, width = 380,borderwidth = 3, background = "darkgrey")
entryRight.place(x = 450, y = 250, width = 380, height = 200)

def modifyfunction():
    global modifyImg
    modifyImg= ImageTk.PhotoImage(Image.open("new_img.jpg"))
    label_img = tk.Label(entryRight, image = modifyImg)
    label_img.pack()
    entryRight.pack(label_img)

def clear():
    global entryRight
    entryRight.destroy()
    entryRight = tk.Entry(gui, width = 380,borderwidth = 3, background = "darkgrey")
    entryRight.place(x = 450, y = 250, width = 380, height = 200)
    

modifyButtonLabel = tk.Label(gui, text = "User Click to modify Orginal Image ", bg = "lightsteelblue", fg = "black", font = ("Monaco", 15)) 
modifyButtonLabel.place(x = 480, y = 220)

#create a display button for user to click
modifyButton = tk.Button(height = 1, width = 2, command = modifyfunction, text = "modify")
modifyButton.place(x = 550, y = 460, width = 60, height = 30)

clearButton = tk.Button(height = 1, width = 2, command = clear, text = "clear")
clearButton.place(x = 670, y = 460, width = 60, height = 30)


gui.mainloop()















