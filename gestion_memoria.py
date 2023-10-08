algoritmo = False

while algoritmo == False:

    print("")
    print("")
    print("Bienvenido al pagrama de Gestion de memoria.")
    print("_____________________________________________")
    print("")
    print("Escoje una opcion.")
    print("0. FIFO")
    print("1. Reloj")
    print("2. NRU")
    op_algoritmo = int(input())

    if op_algoritmo == 0:
        # Función para imprimir el estado actual de la memoria
        def imprimir_memoria():
            print("Memoria actual: ", end="")
            for pagina, proceso in memoria:
                print("({}:{})".format(pagina, proceso), end=" ")
            print("\n")

        # Inicializamos la lista de memoria y la lista de páginas ya presentes en la memoria
        memoria = []
        paginas_en_memoria = []
        opcion_correcta = False;




        while opcion_correcta == False:
            print("")
            print("Bienvenido al algoritmo de FIFO.")
            print("Porfavor escoje si quieres usar datos pre-cargados o quieres ingresarlos tu mismo")
            print("0. Datos PreCargados. ")
            print("1. Ingresar Datos. ")
            op = int(input())
            #validamos la opcion
            if op == 0:
                # Datos a importar
                datos = [(7,0),(0,1),(1,2),(2,3),(0,4),(3,5),(0,6),(4,7),(2,8),(3,9),(0,'A'),(3,'B'),(2,'C'),(1,'D'),(2,'E'),(0,'F')]  
                opcion_correcta = True 
            elif op == 1:
                datos = []
                num_procesos = int(input("Ingrese el número de procesos: "))
                for i in range(num_procesos):
                    pagina = int(input("Ingrese la página {}: ".format(i+1)))
                    proceso = input("Ingrese el proceso {}: ".format(i+1))
                    datos.append((pagina, proceso))
                opcion_correcta = True
            else:
                print("Opcion Incorrecta, Vuelve a intentarlo")

        # Iteramos sobre los datos de entrada
        for pagina, proceso in datos:
            # Verificamos si la página ya está en memoria
            if pagina in paginas_en_memoria:
                print("La página ({}:{}) ya está en memoria. Se ignorará esta inserción.".format(pagina, proceso))
            else:
                # Verificamos si la memoria está llena
                if len(memoria) == 3:
                    # Si la memoria está llena, eliminamos la página más antigua
                    pagina_a_eliminar, proceso_a_eliminar = memoria.pop(0)
                    paginas_en_memoria.remove(pagina_a_eliminar)
                    print("Se eliminó la página ({}:{}) de la memoria.".format(pagina_a_eliminar, proceso_a_eliminar))
                # Insertamos la nueva página en la memoria
                memoria.append((pagina, proceso))
                paginas_en_memoria.append(pagina)
                print("Se insertó la página ({}:{}) en la memoria.".format(pagina, proceso))
            imprimir_memoria()
    
    
    elif op_algoritmo == 1:
        # Inicializamos la lista de memoria, la lista de bits de referencia y el índice del reloj
        memoria = []
        bits_referencia = []
        indice_reloj = 0



        opcion_correcta = False;




        while opcion_correcta == False:
            print("")
            print("Bienvenido al algoritmo de Paginas Reloj.")
            print("Porfavor escoje si quieres usar datos pre-cargados o quieres ingresarlos tu mismo")
            print("0. Datos PreCargados. ")
            print("1. Ingresar Datos. ")
            op = int(input())

            #validamos la opcion
            if op == 0:
                # Páginas a ingresar
                paginas = ['Y', 'Z', 'A', 'B', 'Z', 'C', 'Z', 'D']  
                opcion_correcta = True;
            elif op == 1:
                paginas = []
                num_procesos = int(input("Ingrese el número de procesos: "))
                opcion_correcta = True
                for i in range(num_procesos):
                    pagina = input("Ingrese la página {}: ".format(i+1))
                    paginas.append(pagina)
            else:
                print("Opcion Incorrecta, Vuelve a intentarlo")



        # Función para imprimir el estado actual de la memoria y los bits de referencia
        def imprimir_estado():
            
            print("Estado actual:")
            for i, (pagina, _) in enumerate(memoria):
                print("  Mem[{}]: {} Uso de referencia: {}".format(i, pagina, bits_referencia[i]))
            print("")

        # Iteramos sobre las páginas a ingresar
        for pagina in paginas:
            # Verificamos si la página ya está en memoria
            if pagina in [p for p, _ in memoria]:
                # Marcamos el bit de referencia correspondiente a la página
                i = [i for i, (p, _) in enumerate(memoria) if p == pagina][0]
                bits_referencia[i] = 1
                print("Se marcó el bit de referencia de la página {}".format(pagina))
            else:
                # Verificamos si la memoria está llena
                if len(memoria) < 3:
                    # Si la memoria no está llena, simplemente agregamos la página a la memoria
                    memoria.append((pagina, 1))
                    bits_referencia.append(1)
                    print("Se agregó la página {} a la memoria".format(pagina))
                else:
                    # Si la memoria está llena, buscamos la página con el bit de referencia a cero y la reemplazamos
                    while True:
                        # Si el bit de referencia del índice actual del reloj es uno, lo marcamos como cero y pasamos al siguiente índice
                        if bits_referencia[indice_reloj] == 1:
                            bits_referencia[indice_reloj] = 0
                            indice_reloj = (indice_reloj + 1) % len(memoria)
                            #el % len(memoria) se usa para cuando el conteo supera el tamaño de la lista volver a 0
                        # Si el bit de referencia del índice actual del reloj es cero, reemplazamos la página y marcamos el bit de referencia como uno
                        else:
                            pagina_a_reemplazar, _ = memoria[indice_reloj]
                            memoria[indice_reloj] = (pagina, 1)
                            bits_referencia[indice_reloj] = 1
                            print("Se reemplazó la página {} por {}".format(pagina_a_reemplazar, pagina))
                            # Avanzamos el índice del reloj y salimos del ciclo
                            indice_reloj = (indice_reloj + 1) % len(memoria)
                            break
            imprimir_estado()
    
    
    elif op_algoritmo == 2:
                

        #Tamaño de la memoria
        tamano = 3
        memoria = []

        contador_cambios = 0
        opcion_correcta = False;




        while opcion_correcta == False:
            print("")
            print("Bienvenido al algoritmo de NRU.")
            print("Porfavor escoje si quieres usar datos pre-cargados o quieres ingresarlos tu mismo")
            print("0. Datos PreCargados. ")
            print("1. Ingresar Datos. ")
            op = int(input())
            
            #validamos la opcion
            if op == 0:
                #espesificamos los datos precargados
                data = [(7,1,0),(0,1,0),(1,1,1),(2,1,1),(0,1,0),(3,1,1),(0,1,0),(4,1,1),(2,1,1),(3,1,0),(0,1,0),(3,1,0),(2,1,1),(1,1,0),(2,1,0)]
                opcion_correcta = True
            elif op == 1:
                data = []
                num_procesos = int(input("Ingrese el número de procesos: "))
                for i in range(num_procesos):
                    pagina = int(input("Ingrese la página {}: ".format(i+1)))
                    referencia = int(input("Ingrese indice de referencia {}: ".format(i+1)))
                    modificado = int(input("Ingrese indice de modificado {}: ".format(i+1)))
                    data.append((pagina, referencia, modificado))
                opcion_correcta = True
            else:
                print("Opcion Incorrecta, Vuelve a intentarlo")



        for pagina, referencia, modificacion in data:
            encontrado = False
            for i, (p, r, m) in enumerate(memoria):
                if pagina == p:
                    encontrado = True
                    if r == 0:
                        memoria[i] = (pagina, 1, m)
                    break

            if not encontrado:
                if len(memoria) < tamano:
                    memoria.append((pagina, referencia, modificacion))
                else:
                    gerarquia_minima = None
                    index_gerarquia_minima = None
                    index_menor_antiguedad = None
                    for i, (p, r, m) in enumerate(memoria):
                        gerarquia = r + m
                        if gerarquia_minima is None or gerarquia < gerarquia_minima:
                            gerarquia_minima = gerarquia
                            index_gerarquia_minima = i
                            index_menor_antiguedad = i
                        elif gerarquia == gerarquia_minima:
                            index_menor_antiguedad = i if memoria[i][1] < memoria[index_menor_antiguedad][1] else index_menor_antiguedad

                    memoria[index_menor_antiguedad] = (pagina, referencia, modificacion)
            
            contador_cambios += 1
            if contador_cambios == 4:
                contador_cambios = 0
                for i, (p, r, m) in enumerate(memoria):
                    memoria[i] = (p, 0, m)
                    
            print("")
            print("La pagina que se esta ingresando es: ["+str(pagina)+", "+str(referencia)+", "+str(modificacion)+"]")
            print("Estado de la memoria completa:", memoria)

    else:
        print("Opcion Incorrecta, Vuelve a intentarlo")


