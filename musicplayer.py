import pygame
from pygame import mixer
from tkinter import*
from tkinter import Tk
import os
def playmysong():
    currentsong=playlist.get('active')
    print(currentsong)
    pygame.mixer.music.load("/root/Music/11.mp3")
    songstatus.set('PLAYING')
    pygame.mixer.music.play()


def PauseSong():
    songstatus.set("PAUSE")
    mixer.music.pause()

def StopSong():
    songstatus.set("STOP")
    mixer.music.stop()

def ResumeSong():
    songstatus.set("RESUME")
    mixer.music.unpause()

root = Tk()
root.title("Music Player")
mixer.init()
songstatus=StringVar()
songstatus.set("CHOOSING")

playlist=Listbox(root,selectmode=SINGLE,bg="blue",fg="black",font=('arial',15),width=60)
playlist.grid(columnspan=5)

path ="/root/Music"
songs=os.listdir(path)
for s in songs:
    playlist.insert(END,s)

playbutton=Button(root,text='PLAY',command=playmysong)
playbutton.config(font=('arial',20),bg="green",fg="black",padx=7,pady=7)
playbutton.grid(row=1,column=0)

playbutton=Button(root,text='PAUSE',command=PauseSong)
playbutton.config(font=('arial',20),bg="red",fg="black",padx=7,pady=7)
playbutton.grid(row=1,column=1)

playbutton=Button(root,text='STOP',command=StopSong)
playbutton.config(font=('arial',20),bg="yellow",fg="black",padx=7,pady=7)
playbutton.grid(row=1,column=2)

playbutton=Button(root,text='RESUME',command=ResumeSong)
playbutton.config(font=('arial',20),bg="pink",fg="black",padx=7,pady=7)
playbutton.grid(row=1,column=3)

mainloop()