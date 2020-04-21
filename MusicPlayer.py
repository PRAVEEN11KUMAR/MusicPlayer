from pygame import mixer

root = Tk()

mixer.init()

root.geometry('300x300')
root.title("Melody")

text = Label(root, text='Lets make some noise!')
text.pack()
def play_music():
    mixer.music.load("yenoo.mp3")
    mixer.music.play()

playBtn = Button(root,text="Play", command=play_music)
playBtn.pack()

root.mainloop()
