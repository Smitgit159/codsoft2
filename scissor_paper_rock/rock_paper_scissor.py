from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

#picture 
rock_img = ImageTk.PhotoImage(Image.open("rock image (1).png"))
paper_img = ImageTk.PhotoImage(Image.open("paper_img (1).png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissor_img (1).png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock image (2).png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_img (2).png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_img (2).png"))

#insert picture
user_label = Label(root,image=scissor_img,bg="#9b59b6")
comp_label = Label(root,image=scissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerscore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)
playerscore.grid(row=1,column=3)

#messages
msg = Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)


#update message
def updateMessage(x):
    msg['text'] = x

#update user score
def updateuserscore():
    score = int(playerscore["text"])
    score += 1
    playerscore["text"] = str(score)

#update computer score

def updatecompscore():
    score = int(computerscore["text"])
    score += 1
    computerscore["text"] = str(score)

#check winner
def checkwin(player,computer):
    if player == computer:
        updateMessage("Its a tie!!!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You loose")
            updatecompscore()
        else:
            updateMessage("You win")
            updateuserscore
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You loose")
            updatecompscore()
        else:
            updateMessage("You win")
            updateuserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You loose")
            updatecompscore()
        else:
            updateMessage("You win")
            updateuserscore()
    else:
        pass
    
    

#update choices

choices = ["rock","paper","scissor"]





def updatechoice(x):
    
#for computer
    compchoice = choices[randint(0,2)]
    if compchoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    
    
    
#for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
        
    checkwin(x,compchoice)
       
    


    
    


#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command =lambda:updatechoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command = lambda:updatechoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command = lambda:updatechoice("scissor")).grid(row=2,column=3)



root.mainloop()




