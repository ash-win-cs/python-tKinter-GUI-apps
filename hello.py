from tkinter import *

root = Tk()
root.title("Hello World!")
root.geometry("400x400")

#clicked function
def clicked():
    my_label2 = Label(root, text="Youclicked the button!").grid()
    

my_label = Label(root, text = "HELLO WORLD", fg = "blue", bg = "black", font = ("algerian", 22))
my_label.grid(row= 0,column=0, columnspan = 2)       #sticky moves the element to any side of the column W:west E:East

my_label2 = Label(root, text = "hello wonderful", relief = "ridge", font = ("arial", 11))
my_label2.grid(row=1,column=0)

my_label3 = Label(root, text = "first box", relief = "ridge", font = ("arial", 10))
my_label3.grid(row=1,column=1)

my_button = Button(root, text = "Click me!", command=clicked())
my_button.grid(row=2,column=0,pady=20)


root.mainloop()