def ispalindrome(word:str)->bool:
    word = word.replace(" ","").lower()
    print("Un palindromo es una palabra que tiene las letras en el mismo orden al derecho y al revez")

    if word == word[::-1]:
        print("Es una palindromo ")
    else:
        print("No es un palindromo")
    return word == word[::-1]
    

def run():
    
    ispalindrome(1000)

if __name__ == "__main__":
     run()