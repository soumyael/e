import tkinter
from functools import partial
from functions import *



class Interface:
    #a chaque moment ou on va creer une nouvelle instance  de l'interface la window
    def __init__(self, window):
        self.window=window
    def cryptMessage(self):
        tkinter.Label(self.window, text="SESSION DE CRYPTAGE DE MESSAGES ",bg='gray',fg='white', font=('Helvetica',20)).pack()

        #afficher les elements en rappot avec le message à entrer
        tkinter.Label(self.window, text="Entrer le message : ", bg='gray',fg='white', font=('Helvetica',15)).place(x=20,y=100)
        entry_message = tkinter.Entry(self.window,bg='gray',fg='white', font=('Helvetica',15), width=35)
        entry_message.place(x=200,y=100)

        #afficher les elements en rapport avec la cle de chiffrement
        tkinter.Label(self.window, text="Entrer la clé : ", bg='gray', fg='white', font=('Helvetica', 15)).place(x=20,y=150)
        entry_key = tkinter.Entry(self.window, bg='gray', fg='white', font=('Helvetica', 15),width=35)
        entry_key.place(x=200, y=150)
        #afficher le bouton
        tkinter.Button(self.window,text="CRYPTER",bg='gray', fg='white', font=('Helvetica', 15),command=partial(self.get_data,entry_message,entry_key)).place(x=500, y=200)

        #afficher le message crypte à l'utilisateur
        tkinter.Label(self.window, text="le résultat est : ", bg='gray', fg='white', font=('Helvetica', 15)).place(x=20,y=300)
        self.insert=tkinter.Entry(self.window, bg='gray', fg='white', font=('Helvetica', 15),width=35)
        self.insert.place(x=150, y=300)

    def decryptMessage(self):
        tkinter.Label(self.window, text="SESSION DE DECRYPTAGE DE MESSAGES ",bg='gray',fg='white', font=('Helvetica',20)).pack()

        #afficher les elements en rappot avec le message à entrer
        tkinter.Label(self.window, text="Entrer le message : ", bg='gray',fg='white', font=('Helvetica',15)).place(x=20,y=100)
        entry_message = tkinter.Entry(self.window,bg='gray',fg='white', font=('Helvetica',15), width=35)
        entry_message.place(x=200,y=100)

        #afficher les elements en rapport avec la cle de chiffrement
        tkinter.Label(self.window, text="Entrer la clé : ", bg='gray', fg='white', font=('Helvetica', 15)).place(x=20,y=150)
        entry_key = tkinter.Entry(self.window, bg='gray', fg='white', font=('Helvetica', 15),width=35)
        entry_key.place(x=200, y=150)
        #afficher le bouton
        tkinter.Button(self.window,text="DECRYPTER",bg='gray', fg='white', font=('Helvetica', 15),command=partial(self.get_data,entry_message,entry_key,False)).place(x=500, y=200)

        #afficher le message crypte à l'utilisateur
        tkinter.Label(self.window, text="le résultat est : ", bg='gray', fg='white', font=('Helvetica', 15)).place(x=20,y=300)
        self.insert=tkinter.Entry(self.window, bg='gray', fg='white', font=('Helvetica', 15),width=35)
        self.insert.place(x=150, y=300)


    def get_data(self,entry_message,entry_key,isCreypt=True):
        message=entry_message.get()
        resultat=""
        key=entry_key.get()

        if isCreypt:
        #print(f"Le message est : {message} et La clé est : {key}")
            resultat=crypt(message,key)
        else:
            resultat=decrypt(message,key)

        self.insert.delete(0,tkinter.END)
        self.insert.insert(0,resultat)