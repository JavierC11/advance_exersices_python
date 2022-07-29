#This is the same exercise done in Iterators but with another structure.
import time
import os

def fibonacci(limit_time: int ):
    timel = limit_time
    n1=0
    n2=1
    counter = 0
    timel = timel + time.time()
    while True:        
        if timel <= time.time():
            print("El tiempo de ejecuccion se acabo.")
            exit()
        elif counter == 0 :
            counter += 1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            nsum = n1+n2
            n1, n2 = n2, nsum
            counter +=1
            yield nsum


if __name__ == "__main__":
    limite =  int(input("Ingresa el limite de tiempo que tiene la funcion para ajecutarse. "))  
    fibo = fibonacci(limite)
    for element in fibo:
        print(element)
        time.sleep(1) 