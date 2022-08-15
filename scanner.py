import sys
import os
import time


def run():
    ##IoMenu
    os.system("clear")
    words_list = {}
    print("\n🟢 By: Javier Castillo 5190-19-7011")
    print("***********************************")
    print("***********************************")
    print("🚀Bienvenido al programa Scanner🚀")
    
    ##Estadandarizamos la palabra
    print("\n\n🟢porfavor ingresa la palabra que \nquieres descomponer en caracteres: ")
    word = sys.stdin.read()
    word = word.lower()
    nword = 0
    # nspace = 0
    # njums = 0

    for i in range(0,len(word)):
        aux = 0 
        valueaux = 1    
        for key, value in words_list.items(): 
            if word[i] == key:
                value = value + 1
                aux = value
        if aux ==0:
            valueaux = valueaux +  aux
            words_list[word[i]] = (valueaux)
        else:
            words_list[word[i]] = (aux)

    #En este codigo contamos las palabras que tiene nuestro string recibido
    nword = 1
    nlines = 1
    for i in range(0,len(word)):
        if i+1 != len(word):       
            if (word[i] == " " and word[i+1] != " ") or (word[i] == "\n" and word[i+1] != " "):
                nword+= 1
            elif word[i] == "\n":
                nlines += 1



    #Mostramos la palabra para tener una referencia de lo que tenemos que descomponer en caracteres,
    #tambien agregamos un "." al final para poder saber si hay espacios despues de la ultima palabra.
    print("\n🟢La palabra ha descomponer es \n👉 "+word+".\n")
    #Mostradmos todas las latras cambiando los espacios " " por la palabra "Espacio"
    #como se inidico en el ejercicio.
    for key, value in words_list.items():
        if key == " ":
            # nspace += 1
            print("Espacio 👉 " +str(value))
        elif key == "\n":
            print("Lineas 👉"+str(value))
        else:
            print(key+" 👉 "+str(value))
    print("Palabras 👉 " + str(nword))
    time.sleep(10)
    
    
    

if __name__ == "__main__":
    run()