#this program is to add icon to the window from default
#Entry widgets
from tkinter import *

root = Tk()
root.title("Entry widgets")
root.geometry("400x400")
root.iconbitmap("C:/Users/acer/Documents/gui/enigma.ico")

#create click function
def clicked():
    my_label2 = Label(root, text= "Hello " + e.get())
    my_label2.pack()
    

#Create label widget
my_label = Label(root, text="Entry Widgets", fg="white", bg="black", font=("algerian", 22)).pack()

#Create label widget
my_label1 = Label(root, text="Enter your name: ").pack()

#Create entry widget
e = Entry(root, font=("Helvetica",10))
e.pack(pady=10)

#create Buttons
my_button = Button(root, text="Button", command=clicked).pack()


root.mainloop()