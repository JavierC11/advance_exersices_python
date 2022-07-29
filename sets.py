grupo_a = {2,3, "Adios",0, (1,2,3), (2,3,4)}
grupo_b = {"Adios",5, True, False,  (1,2,3)}

def remove_duplicates(some_list: list) -> list:
    # mylist = []
    # for element in some_list:
    #     if element not in mylist:
    #         mylist.append(element)
    # return mylist
    #      ⬇️ 
    # Toda la logica de nuestro for esta en la estructura set()
    return list(set(some_list))

def run():
    #print(remove_duplicates([1,1,1,2,2,2,3,3,3,4,5]))
    grupo_grupo = grupo_a & grupo_b
    print(grupo_grupo)

    grupo_grupo2 = grupo_a | grupo_b
    print(grupo_grupo2)

    grupo_grupo3 = grupo_a - grupo_b
    print(grupo_grupo3)

    grupo_grupo4 = grupo_a ^ grupo_b
    print(grupo_grupo4)




if __name__ == "__main__":
    run()                               