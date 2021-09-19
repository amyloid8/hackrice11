from tkinter import *


def click():
    entered_text=textentry.get()


rmgui=Tk()
rmgui.title("Title")

#image
rmgui.configure(background="#8C7284")
photo1=PhotoImage(file=r"C:\Users\amyda\Documents\Rice University\hackrice11\IMG_0051.gif")
photo1 = photo1.zoom(25) #with 250, I ended up running out of memory
photo1 = photo1.subsample(32) #mechanically, here it is adjusted to 32 instead of 320

Label (rmgui, image=photo1, bg="#8C7284") .grid(row=0, column=0, sticky=N)

#name
Label (rmgui, text="What's your name?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=2, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=3, column=0, sticky=N)

#year
Label (rmgui, text="What's your YOG?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=4, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=5, column=0, sticky=N)
#major
Label (rmgui, text="What's your major?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=6, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=7, column=0, sticky=N)
#temp
Label (rmgui, text="What's your preferred room temperature?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=10, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=11, column=0, sticky=N)
#numPpl
Label (rmgui, text="How many roommates are you looking for?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=12, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=13, column=0, sticky=N)
#sleep
Label (rmgui, text="What's your sleep schedule like?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=16, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=17, column=0, sticky=N)
#bio
Label (rmgui, text="Do a bio?", bg="#8C7284", fg="white", font="none 10 bold") .grid(row=18, column=0, sticky=N)
textentry=Entry(rmgui, width=20, bg="white")
textentry.grid(row=19, column=0, sticky=N)
#submission
Button(rmgui, text="FIND YOUR ROOMMATE!", width=20, command=click) .grid(row=20, column=0, sticky=N)


rmgui.mainloop()

