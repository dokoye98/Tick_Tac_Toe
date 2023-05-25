from tkinter import *
import Functions
import random
root = Tk()
root.configure(bg="red")
root.geometry(f'{Functions.height}x{Functions.width}')
root.title("Tick Tac Toe")
players = ["X","O"]
player =  random.choice(players)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
labels = Label(text=player + " turn")
labels.pack(side= "top")
#root.resizable(False,False)

top_frame = Frame(root,bg="black",width=Functions.widthper(200),height=Functions.heightper(9))
top_frame.place(x=0,y=0)
side_frame = Frame(root,bg="black",width=Functions.widthper(12.5),height=Functions.height)
side_frame.place(x=0,y=0)
center_frame = Frame(root, height=Functions.heightper(2.6),width= Functions.widthper(5))
center_frame.place(x=Functions.widthper(15),y=Functions.heightper(15))
bt = Button(center_frame, bg= "white",text="hello" )
frame = Frame(root)
frame.pack()

#this runs the window 
root.mainloop()