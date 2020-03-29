#Entry widgets
from tkinter import *

root = Tk()
root.title("Entry widgets")
root.geometry("400x400")


#create click function
def clicked():
    my_label2 = Label(root, text="Value Recorded").pack()
    

#Create label widget
my_label = Label(root, text="Entry Widgets", fg="white", bg="black", font=("algerian", 22)).pack()

#Create entry widget
e = Entry(root)
e.pack(pady=10)

#create Buttons
my_button = Button(root, text="Button", command=clicked).pack()

root.mainloop()