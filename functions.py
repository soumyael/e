from constantes import *

def crypt(mess,key):
    key = int(key)
    messageCrypt=''

    #parcourir le message entrer
    for letter in mess:

        #parcourir toute les lettre de notre alphabet et leur indice
        for index, letter_alpha in alphabets.items():
            if letter==letter_alpha:
                index+= key

                while index>=len(alphabets)-1:
                    index-=len(alphabets)
                messageCrypt += alphabets[index]


    return messageCrypt

def decrypt(message,key):
    key=int(key)
    message_decrypte=""

    for letter in message:
        for index,letter_alpha in alphabets.items():
            if letter==letter_alpha:
                index-=key

                while index <0:
                    index+=len(alphabets)
                message_decrypte+=alphabets[index]


    return message_decrypte





