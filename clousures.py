
def make_division_by(n):
    def division(number2):
        assert type(number2) == int, "Solo puedes hacer esto con numeros enteros"
        return number2/n
    return division



def run():
    division3 = make_division_by(3)
    print(division3(18))

    division5 = make_division_by(5)
    print(division5(100))

    division18 = make_division_by(18)
    print(division18(54))


if __name__ ==  "__main__":
    run()