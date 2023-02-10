from tkinter import *
import random

window = Tk()
window.title("Rock, paper, scissors game.")
window.geometry("700x700")
window.resizable(0, 0)

computer_choice = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissors"
}

user_result = 0
computer_result = 0
b_result = ""
computer_c_choice = "Computer choice: "
label_result = Label(window)
label_c_choice = Label(window)
label_u_result = Label(window)
label_c_result = Label(window)

def p_rock():
    global user_result
    global computer_result
    global b_result
    c_c = computer_choice[str(random.randint(0, 2))]
    if c_c == "Scissors":
        user_result += 1
        b_result = "Player Won!"
    elif c_c == "Paper":
        computer_result += 1
        b_result = "Computer Won..."
    else:
        b_result = "Draw"
    label_result.config(text = b_result)
    label_c_choice.config(text = c_c)
    label_u_result.config(text = user_result)
    label_c_result.config(text = computer_result)
    



def p_paper():
    global user_result
    global computer_result
    global b_result
    c_c = computer_choice[str(random.randint(0, 2))]
    if c_c == "Rock":
        user_result += 1
        b_result = "Player Won!"
    elif c_c == "Scissors":
        computer_result += 1
        b_result = "Computer Won..."
    else:
        b_result = "Draw"
    label_result.config(text = b_result)
    label_c_choice.config(text = c_c)
    label_u_result.config(text = user_result)
    label_c_result.config(text = computer_result)
        
def p_scissors():
    global user_result
    global computer_result
    global b_result
    c_c = computer_choice[str(random.randint(0, 2))]
    if c_c == "Paper":
        user_result += 1
        b_result = "Player Won!"
    elif c_c == "Rock":
        computer_result += 1
        b_result = "Computer Won..."
    else:
        b_result = "Draw"
    label_result.config(text = b_result)
    label_c_choice.config(text = c_c)
    label_u_result.config(text = user_result)
    label_c_result.config(text = computer_result)

def reset():
    global user_result
    global computer_result
    global b_result
    computer_result = 0
    user_result = 0
    label_result.config(text = 0)
    label_c_choice.config(text =  "Computer choice: ")
    label_u_result.config(text =  0)
    label_c_result.config(text =  0)





label_result = Label(window, text = "Who won?", font = 12)
label_result.pack(pady = 10)



label_frame = Frame(window)
label_frame.pack(pady = 100)

label_result_computer = Label(label_frame, text = "Computer result: ", width = 20)
label_result_computer.grid(row = 0, column = 0)
label_c_result = Label(label_frame, text = 0)
label_c_result.grid(row = 1, column = 0)



label_result_user = Label(label_frame, text = "User result: " )
label_result_user.grid(row = 0, column = 1)
label_u_result = Label(label_frame, text = 0)
label_u_result.grid(row = 1, column = 1)



display_frame = Frame(window, height = 1000, width = 1000, highlightbackground="black", highlightcolor="black", highlightthickness="2.5")
display_frame.pack(side = TOP, pady = 1)




image_s = PhotoImage(file = 'scissors.png')
image_p = PhotoImage(file = 'paper.png')
image_r = PhotoImage(file = 'rock.png')

scissors = Button(display_frame, width = 200, image = image_s, command = p_scissors).grid(row = 0, column = 0, padx = 1, pady = 1)
rock = Button(display_frame, font = 10, width = 200, image = image_r, command = p_rock).grid(row = 0, column = 1, padx = 1, pady = 1)
paper = Button(display_frame, font = 10, width = 200, image = image_p, command = p_paper).grid(row = 0, column = 2, padx = 1, pady = 1)





label_c_choice = Label(window, text = "Computer choice: ")
label_c_choice.pack()



reset = Button(text = "Reset Game", command = reset)
reset.pack(side = BOTTOM, pady = 25)   


window.mainloop()