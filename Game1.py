from tkinter import *
import random

def next_turn(row,column):
    global player
    
    if buttons[row][column] == "" and check_winner() is False:
        
        if player == players[0]:
            
            buttons[row][column] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=players[1] + "turn")
            elif check_winner() is True:
                label.config(players[0] + "Wins")
            elif check_winner() == "Tie":
                label.config("Tie")
        else:
            buttons[row][column] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=players[0] + "turn")
            elif check_winner() is True:
                label.config(players[1] + "Wins")
            
            
 
def check_winner():
    
    for row in range(3):
            if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] !="":
                return True
    for column in range(3):
            if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] !="" :
                return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] !="":
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] !="":
        return True
    elif empty_space() is False:
        return "Tie"
    else:
        return False

def empty_space():
    pass


def new_game():
    pass

root = Tk()
root.title("X's and O's")
players = ["X","O"]
player= random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text= player + " turn",font=("consalas",40))
label.pack(side="top")
reset_button = Button(text="Restart",font=("consalas",20),command=new_game())
reset_button.pack(side="top")
frame = Frame(root)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame,text="",font=("consalas",40),width=5,height=2
                                     ,command=lambda row=row, column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

root.mainloop()