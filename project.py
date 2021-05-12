import tkinter as tk
from PIL import Image,ImageTk,ImageFilter



gui = tk.Tk() #create window object
gui.title("Car Display")  #add the title of the window
gui.geometry("1200x700") #resize the window
gui.configure(background = 'slate grey') #set window background color

topLabel = tk.Label(gui, text = "Car Photoshop Showcase", bg = "slate grey", bd = 10, fg = "white", font = ("Castellar", 30)) 
topLabel.pack()

#create a user text input box
textEntry = tk.Text(gui, height = 2, width = 24, bg = 'white', font = ("Castellar", 20))
textEntry.place(x = 60, y = 150)
#create a label of user text input box
textEntryLabel = tk.Label(gui, text = "Enter a Name of Electric Car ", bg = "slate grey", bd = 10, fg = "white", font = ("Castellar", 15)) 
textEntryLabel.place(x = 110, y = 105)

#create a canvas
cv = tk.Canvas(gui,width=700,height=400)
cv.place(x = 400, y = 130)

#use teammate's output
def displayfunction():
    #resize the original pic
    global img
    temp = Image.open("origin.jpg")
    outputFile = temp.resize((700,400),Image.ANTIALIAS)
    outputFile.save("display.jpg")
    #add resized pic to canvas
    img= ImageTk.PhotoImage(Image.open("display.jpg"))
    label_img = tk.Label(cv, image = img)
    label_img.pack()

#the service I provide
def modifyfunction():
    # temp = Image.open("display.jpg")
    playList = [ImageFilter.CONTOUR,
                ImageFilter.EMBOSS,
                ImageFilter.EDGE_ENHANCE_MORE,
                ImageFilter.BLUR,
                ImageFilter.DETAIL,
                ImageFilter.FIND_EDGES,
                ImageFilter.EDGE_ENHANCE,
                ImageFilter.SMOOTH_MORE,
                ImageFilter.SMOOTH,
                ImageFilter.SHARPEN,
                ImageFilter.RankFilter(5,0),
                ImageFilter.MaxFilter(3),
                ImageFilter.MinFilter(3)
                ]

    for i in playList:
        temp = Image.open("display.jpg")
        new_img = temp.filter(i)
        new_img.show()

#create a display button for user to click
displayButton = tk.Button(height = 1, width = 2, command = displayfunction)
displayButton.place(x = 120, y = 230)
#create a label of button 
displayButtonLabel = tk.Label(gui, text = "Button - Display ", bg = "slate grey", bd = 10, fg = "white", font = ("Castellar", 15)) 
displayButtonLabel.place(x = 150, y = 220)

#create a display button for user to click
modifyButton = tk.Button(height = 1, width = 2, command = modifyfunction)
modifyButton.place(x = 120, y = 300)
#create a label of button 
modifyButtonLabel = tk.Label(gui, text = "Button - Modify ", bg = "slate grey", bd = 10, fg = "white", font = ("Castellar", 15)) 
modifyButtonLabel.place(x = 150, y = 290)

#create a drop - down menu
OPTIONS = ["Telsa Model 3", "Tesla Model S", "Tesla Model X", "Tesla Model Y"]
variable = tk.StringVar(gui)
variable.set(OPTIONS[0]) # default value
dropDownMenu = tk.OptionMenu(gui,variable, *OPTIONS)
dropDownMenu.pack()
dropDownMenu.place(x = 115, y = 450)
#create a label of button 
dropDownLabel = tk.Label(gui, text = "Select a Car from Menu ", bg = "slate grey", bd = 10, fg = "white", font = ("Castellar", 12)) 
dropDownLabel.place(x = 100, y = 410)
#select from options
def ok():
    print ("value is:" + variable.get())

optionButton = tk.Button(gui, text="OK", command=ok)
optionButton.place(x = 280, y = 451)

gui.mainloop()














