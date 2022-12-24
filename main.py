from tkinter import *
import random as ra
from tkinter import messagebox
r = Tk()
r.title("Color Randomizer Game")
r.geometry("500x500")
r.config(bg="white")
lbl = Label(r,font=("Roman",10),bg="white")
lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
lblscore = Label(r,text="Score: 0",font=("Corbel Light",10),bg="white")
lblscore.place(relx=0.1,rely=0.1,anchor=CENTER)
inputValue = Entry(r)
inputValue.place(relx=0.5,rely=0.6,anchor=CENTER)
#Logic-
class Game():
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["RED","YELLOW","ORANGE","GREEN","BLUE","PURPLE","BROWN","BLACK"]
        self.random_number_for_text = ra.randint(0,7)
        self.colors = ["red","yellow","orange","green","blue","purple","brown","black"]
        self.random_number_for_colors = ra.randint(0,7)
        self.bg = ["red","yellow","orange","green","blue","purple","brown","black"]
        self.random_number_for_bg = ra.randint(0,7)
        self.rt = self.text[self.random_number_for_text]
        self.rc = self.colors[self.random_number_for_colors]
        lbl['text'] = self.rt
        lbl["fg"] = self.rc
        g = self.bg[self.random_number_for_bg]
        lblscore['bg'] = str(g)
        lbl['bg'] = str(g)
        r.config(bg=str(g))
    def __update_score(self,input_value):
        if (input_value == self.colors[self.random_number_for_colors]):
            print(self.colors[self.random_number_for_colors])
            self.__score = self.__score + ra.randint(1,10)
            lblscore['text'] = "Score: "+str(self.__score)
    def get_user_value(self,input):
        self.__update_score(input)
obj = Game()
def getInput():
    v = inputValue.get()
    obj.get_user_value(v)
    obj.updateGame()
    inputValue.delete(0,END)

btn = Button(r,text="Start",command=obj.updateGame,bg="white",fg="blue",relief=FLAT,padx=10,pady=1,font=("Arial",15))
btn.place(relx=0.7,rely=0.8,anchor=E)
btn1 = Button(r,text="Check",command=getInput, bg="white",fg="black",relief=FLAT,padx=10,pady=1)
btn1.place(relx=0.3,rely=0.8,anchor=W)
r.mainloop()