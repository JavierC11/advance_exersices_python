import sys
import os
import time

#funcion Helper para contar las palabras de cada linea de nuestro string
def count_words(word: str):
    nword = 1
    for i in range(0,len(word)):
        if i+1 != len(word):       
            if (word[i] != " " and word[i+1] == " "):
                nword+= 1
                aux = nword
            elif word[i] == "\n":
                pass
    return nword

#funcion principal
def run():
    ##IoMenu
    os.system("clear")
    words_list = {}
    print("\n🟢 By: Javier Castillo 5190-19-7011")
    print("***********************************")
    print("***********************************")
    print("🚀Bienvenido al programa Scanner🚀")
    
#Estadandarizamos la palabra
    print("\n\n🟢porfavor ingresa la palabra que \nquieres descomponer en caracteres: ")
    word = sys.stdin.read().lower()
    nword = 0
    
#ingresamos todas las letras a nuestro diccionario de python
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
    for i in range(0,len(word)):
        if i+1 != len(word):       
            if (word[i] == " " and word[i+1] != " ") or (word[i] == "\n" and word[i+1] != " "):
                nword+= 1

#Patitmos nuestro texto en lineas y contamos las palabras de cada linea con ayuda de nuestras funciones.
    print("\n\n")
    sentence = word.split("\n")
    i = 1
    for linenum in range(0,len(sentence)-1):
        nwords=count_words(sentence[linenum])
        print("👉 "+str(nwords)+" Palabras en linea numero "+str(i))
        i+=1

#listamos todas las palabras dentro de nuestro diccionario
    for key, value in words_list.items():
        if key == " ":
            # nspace += 1
            print("Espacios 👉 " +str(value))
        elif key == "\n":
            print("Lineas 👉"+str(value))
        else:
            print(key+" 👉 "+str(value))
    print("Palabras totales👉 " + str(nword))
    time.sleep(10)
    
    
    

if __name__ == "__main__":
    run()