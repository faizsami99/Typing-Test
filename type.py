import tkinter
import random
import tkinter.messagebox as msg

def Generating_world_list():
    with open("words.txt", "r") as my_file:
        string = my_file.read()
        world_list = string.split("\n")
        return world_list

######variable start
world_list = Generating_world_list()
random.shuffle(world_list)
score = 0
miss = 0
timeleft = 60
######variable end

def start(event):
    global world_list, score, miss
    if timeleft == 60:
        timee()
    hintLebel.config(text="")
    if wordEntry.get() == startlabel['text']:
        score += 1
        scorecount.config(text=score)
    else:
        miss += 1
    random.shuffle(world_list)
    startlabel.config(text=world_list[0])
    wordEntry.delete(0,"end")

def timee():
    global timeleft, score, miss
    if timeleft > 0:
        timeleft -= 1
        timecount.config(text=timeleft)
        timecount.after(1000, timee)
    else:
        hintLebel.config(text="Hit = {}| miss {} | You get {}".format(score, miss, score-miss))
        retry = msg.askretrycancel("Notication","want to retry")
        if retry == True:
            score = 0
            timeleft = 60
            miss = 0
            timecount.config(text=timeleft)
            scorecount.config(text=score)
            hintLebel.config(text="Lets play again")


main_frame = tkinter.Tk()
main_frame.geometry("800x600")
main_frame.title("Typing-master")
main_frame.resizable(0,0)
main_frame.config(bg="powder blue")

introLabel = tkinter.Label(main_frame, text="Welcome to the Typing game", font="arial 25 bold",bg="powder blue", fg="green")
introLabel.place(x=150,y=10)


startlabel = tkinter.Label(main_frame, text=world_list[0], font="arial 40 bold", bg="powder blue")
startlabel.place(x=300, y=200)

wordEntry = tkinter.Entry(main_frame, font="arial 20 bold", bd=10, justify="center")
wordEntry.place(x=220, y=280)
wordEntry.focus_set()
wordEntry.bind("<Return>", start)

scoreLabel = tkinter.Label(main_frame,text="Your score: ", font="arial 25 bold", bg="powder blue", fg="red")
scoreLabel.place(x=20,y=70)

scorecount = tkinter.Label(main_frame, text=score, font="arial 30 bold", bg="powder blue", fg="red")
scorecount.place(x=90, y=140)

timeLable = tkinter.Label(main_frame, text="Time left:", font="arial 25 bold", bg="powder blue", fg="red")
timeLable.place(x=600, y=70)

timecount = tkinter.Label(main_frame, text=timeleft, font="arial 25 bold", bg="powder blue", fg="red")
timecount.place(x=650, y=140)


hintLebel = tkinter.Label(main_frame, text="Type Word and hint Enter", font="arial 40 bold", bg="powder blue", fg="grey")
hintLebel.place(x=80, y=380)

main_frame.mainloop()


