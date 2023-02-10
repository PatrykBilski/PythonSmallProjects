from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("500x500")
window.resizable(0, 0)
window.title("My first calculator with interactive window!")


value = ""

input_text = StringVar()

def btn_click(item):
    global value
    value = value + str(item)
    input_text.set(value)

def btn_clear():
    global value
    value = ""
    input_text.set("")

def btn_del_last():
    global value
    value = value[:-1]
    input_text.set(value)



def btn_equal():
    try:
        global value
        result = str(eval(value))
        input_text.set(result)
        value = ""

    except:
        input_text.set("Error")
        value = ""


input_frame = Frame(window, height = 100, width = 500, highlightbackground="black", highlightcolor="black", highlightthickness="2.5")
input_frame.pack(side=TOP)

input_box = Entry(input_frame, font = ('arial', 18, 'bold'), textvariable = input_text, width = 50, bg ="grey", justify = RIGHT)
input_box.grid(column = 0, row = 0)
input_box.pack(ipadx = 10, ipady = 10)


btn_input = Frame(window, height = 400, width = 500, background= "grey", highlightbackground="black", highlightcolor="black", highlightthickness="2.5")
btn_input.pack()


# First button row
clear = Button(btn_input, text = 'C', width = 16, height = 5, command = lambda: btn_clear()).grid(row = 0, column = 0, padx = 1, pady = 1)
divide = Button(btn_input, text = '/', width = 16, height = 5, command = lambda: btn_click("/")).grid(row = 0, column = 1, padx = 1, pady = 1)
sqrt = Button(btn_input, text = '%', width = 16, height = 5, command = lambda: btn_click("sqrt")).grid(row = 0, column = 2, padx = 1, pady = 1)
exp = Button(btn_input, text = '^', width = 16, height = 5, command = lambda: btn_click("^")).grid(row = 0, column = 3, padx = 1, pady = 1)

one = Button(btn_input, text = '1', width = 16, height = 5, command = lambda: btn_click(1)).grid(row = 1, column = 0, padx = 1, pady = 1)
two = Button(btn_input, text = '2', width = 16, height = 5, command = lambda: btn_click(2)).grid(row = 1, column = 1, padx = 1, pady = 1)
three = Button(btn_input, text = '3', width = 16, height = 5, command = lambda: btn_click(3)).grid(row = 1, column = 2, padx = 1, pady = 1)
times = Button(btn_input, text = '*', width = 16, height = 5, command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

four = Button(btn_input, text = '4', width = 16, height = 5, command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btn_input, text = '5', width = 16, height = 5, command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btn_input, text = '6', width = 16, height = 5, command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
plus = Button(btn_input, text = '+', width = 16, height = 5, command = lambda: btn_click("+")).grid(row = 2, column = 3, padx = 1, pady = 1)

seven = Button(btn_input, text = '7', width = 16, height = 5, command = lambda: btn_click(7)).grid(row = 3, column = 0, padx = 1, pady = 1)
eight = Button(btn_input, text = '8', width = 16, height = 5, command = lambda: btn_click(8)).grid(row = 3, column = 1, padx = 1, pady = 1)
nine = Button(btn_input, text = '9', width = 16, height = 5, command = lambda: btn_click(9)).grid(row = 3, column = 2, padx = 1, pady = 1)
minus = Button(btn_input, text = '-', width = 16, height = 5, command = lambda: btn_click("-")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = Button(btn_input, text = '0', width = 16, height = 5, command = lambda: btn_click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
dot = Button(btn_input, text = '.', width = 16, height = 5, command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)
equal = Button(btn_input, text = '=', width = 16, height = 5, command = lambda: btn_equal()).grid(row = 4, column = 2, padx = 1, pady = 1)
equal = Button(btn_input, text = 'CE', width = 16, height = 5, command = lambda: btn_del_last()).grid(row = 4, column = 3, padx = 1, pady = 1)



window.mainloop()