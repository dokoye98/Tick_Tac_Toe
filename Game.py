from tkinter import *
import Functions
import random


def new_game():
    pass

def next_turn(row,column):
    global player
    
    if buttons[row][column] == "" and checkwinner() is False:
        
        if player == players[0]:
            
            buttons[row][column]["text"] = player
            
            if checkwinner() is False:
            
                player = players[1]
            
                labels.config(text=(players[1] + " turn"))
            
            elif checkwinner() is True:
                player = players[0]
                labels.config(text=(players[0] + "Wins"))
            elif checkwinner() == "Tie":
                labels.config("Tie")
        else:
            buttons[row][column]["text"] = player
            if checkwinner() is False:
                player = players[0]
                labels.config(text=(players[0] + " turn"))
            elif checkwinner() is True:
                player = players[1]
                labels.config(text=(players[1] + "Wins"))
            

def checkwinner():
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

root = Tk()
root.configure(bg="black")
#root.geometry(f'{Functions.height}x{Functions.width}')
root.title("Tick Tac Toe")
players = ["X","O"]
player =  random.choice(players)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
labels = Label(text=player + " turn")
labels.pack(side= "top")
#root.resizable(False,False)

bt = Button(bg= "white",text="Reset",command=new_game)
bt.pack(side="top")
frame = Frame(root)
frame.pack()
for row in range(3):
    for column in range(3):
        buttons[row][column]= Button(frame,text="",width=47,height=15,
                                  command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row = row,column=column)
root.mainloop()