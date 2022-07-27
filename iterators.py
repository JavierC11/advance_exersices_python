import os
import time
from datetime import datetime


class MyError(Exception):
    pass

class fuboiter():
   

    def __init__(self, limit:int):
        self.limit = limit


    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):

        # rnow = time.time()
        # time_sum = rnow + self.limit_time 
        # print(rnow)   
        # print(time_sum)
        if (self.n1+self.n2) >= self.limit:
            raise StopIteration
            
        elif self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.sum = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.sum
            self.counter+=1
            return self.sum

if __name__ == "__main__":
    # fibonacci = 
    for element in fuboiter(4000000):
        print(element)
        time.sleep(0.5)