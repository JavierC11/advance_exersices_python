import sys

def run():
    print("Ingresa las palabras")
    s= sys.stdin.read()

    for word in s:
        if word == "\n":
            print("Contiene un N")
        print(word)

    print(s)

if __name__ == "__main__":
    run()