from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title('ENDLESS POKEMON CARD GAME')
root.geometry('600x400')
root.configure(background  = 'orange')

pikachu = ImageTk.PhotoImage(Image.open('pikachu.jpg'))
abra = ImageTk.PhotoImage(Image.open('abra.jpg'))
bulbasour = ImageTk.PhotoImage(Image.open('bulbasour.jpg'))
charmender = ImageTk.PhotoImage(Image.open('charmender.jpg'))
Iyvasour = ImageTk.PhotoImage(Image.open('Iyvasour.jpg'))
jigglypuff = ImageTk.PhotoImage(Image.open('jigglypuff.jpg'))
kadabra = ImageTk.PhotoImage(Image.open('kadabra.jpg'))
meowth = ImageTk.PhotoImage(Image.open('meowth.jpg'))
nidoking = ImageTk.PhotoImage(Image.open('nidoking.jpg'))
paras = ImageTk.PhotoImage(Image.open('paras.jpg'))
persion = ImageTk.PhotoImage(Image.open('persion.jpg'))
ratata = ImageTk.PhotoImage(Image.open('ratata.jpg'))
spuirtle = ImageTk.PhotoImage(Image.open('squirtle.jpg'))

player1 = Label(root,text='Player 1',bg='red',fg='white')
place.player1(relx = 0.3,rely = 0.4,anchor = CENTER)

player2 = Label(root,text='Player 2',bg='red',fg='white')
place.player2(relx = 0.6,rely = 0.4,anchor = CENTER)

player1_score = Label(root,text='Player 1 Score',bg='yellow',fg='black')
place.player1_score(relx = 0.3,rely = 0.6,anchor = CENTER)

player2_score = Label(root,text='Player 2 Score',bg='yellow',fg='black')
place.player2_score(relx = 0.6,rely = 0.6,anchor = CENTER)

img = Label(root)
place.img(relx = 0.5,rely = 0.5,anchor=CENTER)

mainloop()
