from tkinter import *

root = Tk()                         #defining TKinter variable
root.title("Hello World!")          #Window tittle
root.geometry("400x400")            #size of window
 

my_label = Label(root, text = "HELLO WORLD", fg = "blue", bg = "black", font = ("algerian", 22))
my_label.grid(row= 0,column=1, columnspan = 2)       #column spans the text into 2 columns
                                                     #sticky moves the element to any side of the column W:west E:East

my_label2 = Label(root, text = "hello wonderful", relief = "ridge", font = ("arial", 11))
my_label2.grid(row=1,column=1)

my_label3 = Label(root, text = "first box", font = ("arial", 10))
my_label3.grid(row=3,column=1)

root.mainloop()