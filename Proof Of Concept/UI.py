#127.0.0.1:57110 supercollider server

# -*- coding: utf-8 -*-
from utility import *
from tkinter import *
from FoxDot1 import *
from FoxDot import *


def clickPlay():
    # outputTest = Label(window, text=str(notes) + 
    #                 '\n'+ str(beats) +
    #                 '\n' + str(cm) + 
    #                 '\n' + str(cmBeats)).grid(row=2, column=0)
    player()
    
    label = Label(window, text='testset')
    label.pack()
    

def clickStop():
    Clock.clear()
    
def saveButton():
    pass
        

window = Tk()
window.title("JM Project 20/21")
window.configure(background='#196ffa')

title = Label(window, text='Algorithmic Music Composition using FoxDot',
              bg='#196ffa', fg='white', font='none 12 bold')
#title.grid(row=0,  columnspan=4, pady=10, padx=50)
title.pack()

playButton = Button(window, text="\u2BC8", width=6, bg='#8eb5f5', fg='#196ffa', activebackground='#196ffa', command=clickPlay)
#playButton.grid(row=1, column=0)
playButton.pack(padx=5, pady=10, side=LEFT)

stopButton = Button(window, text="\u23F9",  width=6, bg='#8eb5f5', fg='#196ffa', activebackground='#196ffa', command=clickStop)
#stopButton.grid(row=1, column=1)
stopButton.pack(padx=5, pady=20, side=LEFT)

saveButton = Button(window, text="Save", width=6, bg='#8eb5f5', fg='#196ffa', activebackground='#196ffa', command=clickPlay)
saveButton.pack(padx=5, pady=20, side=LEFT)

#frame for analysis
frame = Frame(window, width=300, height=120, borderwidth=5, relief=SUNKEN, bg='#8eb5f5')
#frame.grid(row=4, column=0, padx=35, pady=10) #padx to line up with title
frame.pack(padx=5, pady=30, side=BOTTOM)

#, sticky=W, pady=10
#, sticky=W, padx=(50,10), pady=10

notes = note_sequence()
print(notes)
beats = note_beats(notes)
print(beats)
cm = counter_melody(notes)
print(cm)
cmBeats = counter_melodyBeats(cm, beats)
print(cmBeats)





window.mainloop()


