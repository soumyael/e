#package qui va nous permettre de creer une fenetre
import tkinter
from interface import Interface

window = tkinter.Tk()
window.title('crypthon')
window.geometry('650x500')
window.iconbitmap('login.png')
#on peut ici ecrire un nombre qui represente une couleur
window.config(bg='gray')

interface = Interface(window)
#interface.cryptMessage()

interface.decryptMessage()


window.mainloop()


