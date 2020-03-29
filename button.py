from tkinter import *

root = Tk()                         #defining TKinter variable
root.title("Hello World!")          #Window tittle
root.geometry("400x400")            #size of window

#clicked function
def clicked():
    my_label1 = Label(root, text="Youclicked the button!").pack() #



my_button = Button(root, text = "Click me!", command=clicked())
my_button.pack()


root.mainloop()