from random import randint
from datetime import datetime
import os




def make_count_seconds(func):
    def count_seconds(*args, **kwargs):

        beforefun = datetime.now()
        func(*args, **kwargs)
        afterfun = datetime.now()
        functime = afterfun - beforefun
#        print(functime.total_seconds)
        
        return print("This function has ended in " + str(round(functime.total_seconds(),2)) + " Sec🚀.")
    return count_seconds




def make_anotherdecorate(func):
    def anotherdecorate(*args, **kwargs):

        numeros = ["1","2","3","4","5","6","7","8","9"] 
        mayusculas = ["A","B","C","D","E","F","G","H"]
        minusculas = ["a","b","c","d","e","f","g","h"]   
        simbolos = ["/","*","%","@","#","$"]
        conjunto = numeros + mayusculas + minusculas + simbolos
        generatepass = []


        passw = func(*args, **kwargs)
        tt = passw.maketrans("aAiIoOtTsSPpe ","@4!!0077$$99E*")
        passw = passw.translate(tt)

        for i in range(2):
            indice = randint(0,len(conjunto))
            indice = conjunto[indice]
            generatepass.append(indice)
        
        generatepass = ''.join(generatepass)
        passw = passw + generatepass
        return print("\nNow your password is much more secure: -> " + passw +" <- ")
    return anotherdecorate


@make_count_seconds
@make_anotherdecorate
def chosepass():
    os.system("clear")
    print("\n\nEverybody thinks theirs passwords are the best, however all our passwords can be better!! ")
    passw = input("\nPlease type your password: ")
    return passw

@make_count_seconds
#this is only a example
def only():
    for _ in range(1,100000000):
        pass

@make_count_seconds
def sum(a: int, b:int)-> int:
    return a+b



def run():
    chosepass()
    


if __name__ == "__main__":
    run()