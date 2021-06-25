opcion = input('Desea continuar procesando información? Escriba Si/No: ')

cont = 1
encuestado = []
encuestados = []
listaMargenPobreza = ['Muy Pobre','Pobre','Clase Media','Rico','Muy Rico']
contMuyPobre = 0
contPobre = 0
contClaseMedia = 0
contRico = 0
contMuyRico = 0

while opcion.lower() == 'si' and cont <=5:
    print(f'Por favor ingrese la información para el mes #{cont}')
    mes = input('Nombre mes:')
    ingreso = int(input('Ingreso del mes:'))
    personas = int(input('Cantidad de personas que dependen del ingreso:'))

    # Valido margen de pobreza
    if ingreso <= 800000:
        if personas == 1 : margenPobreza = listaMargenPobreza[2]
        elif personas >= 2 and personas <=5 : margenPobreza = listaMargenPobreza[1]
        elif personas >= 6 : margenPobreza = listaMargenPobreza[0]
    elif ingreso > 800000 and ingreso <= 1500000 :
        if personas >= 1 and personas <= 5: margenPobreza = listaMargenPobreza[2]
        elif personas == 6 or personas ==7 : margenPobreza = listaMargenPobreza[1]
        elif personas >= 8 : margenPobreza = listaMargenPobreza[0]
    elif ingreso > 1500000 and ingreso <= 2100000:
        if personas == 1: margenPobreza = listaMargenPobreza[3]
        elif personas >= 2 and personas <= 7 : margenPobreza = listaMargenPobreza[2]
        elif personas >= 8 : margenPobreza = listaMargenPobreza[1]
    elif ingreso > 2100000 and ingreso <= 3000000:
        if personas >= 1 and personas <= 5:  listaMargenPobreza[3]
        elif personas >= 6: margenPobreza = listaMargenPobreza[2]
    elif ingreso > 3000000:
        if personas >= 1 and personas <= 5: listaMargenPobreza[4]
        elif personas == 6 or personas == 7: listaMargenPobreza[3]
        elif personas >= 8 : margenPobreza = listaMargenPobreza[2]

    # Calculo el margen de pobreza mas frecuente
    if margenPobreza == 'Muy pobre' : contMuyPobre += 1
    elif margenPobreza == 'Pobre' : contPobre += 1
    elif margenPobreza == 'Clase Media': contClaseMedia += 1
    elif margenPobreza == 'Rico': contRico += 1
    elif margenPobreza == 'Muy Rico': contMuyRico += 1

    #guardo datos en una lista
    encuestado.append((mes,ingreso,personas,margenPobreza))

    #Despues de ingresar los datos del ultimo mes, hago calculos
    if cont == 5:

        totalIngreso = 0
        maxIngreso = 0
        minIngreso = 0
        contMes = 0

        #Calculo datos finales para un encuestado
        for mes in encuestado:
            #Muestro margen de pobreza para el respectivo mes
            print(f'Para el mes de {mes[0].capitalize()} el margen de pobreza es {mes[3]}.')

            #Sumo el total de ingresos por todos los meses
            totalIngreso += mes[1]

            #Calculo mes con maximo ingreso
            if mes[1] > maxIngreso :
                posMaxIngreso = contMes
                maxIngreso = mes[1]

            #Calculo mes con minimo ingreso
            if contMes == 0:
                minIngreso = mes[1]
                posMinIngreso = 0
            else:
                if mes[1] < minIngreso:
                    posMinIngreso = contMes
                    minIngreso = mes[1]

            contMes += 1

        #Realizo promedio de ingresos
        promedio = totalIngreso / len(encuestado)

        #Muestro resultados finales para este encuestado
        print(f'Para promedio de sus ingresos es de {promedio}')
        print(f'El mes con mayor ingreso fue {encuestado[posMaxIngreso][0]} con un total de {encuestado[posMaxIngreso][1]}')
        print(f'El mes con menor ingreso fue {encuestado[posMinIngreso][0]} con un total de {encuestado[posMinIngreso][1]}')

        #Calculo de margenPobrezaComun
        listaMargenPobrezaComun = [contMuyPobre, contPobre, contClaseMedia, contRico,contMuyRico]

        max_value = max(listaMargenPobrezaComun)
        max_index = listaMargenPobrezaComun.index(max_value)

        #Agrego encuestado a lista con todos los valores calculados
        encuestados.append((encuestado,promedio,encuestado[posMaxIngreso][0],encuestado[posMinIngreso][0],listaMargenPobreza[max_index]))
        opcion = input('Desea continuar procesando información? Escriba Si/No: ')
        if opcion.lower() == 'si':
            cont = 1
            encuestado = []
            contMuyPobre = 0
            contPobre = 0
            contClaseMedia = 0
            contRico = 0
            contMuyRico = 0

    cont += 1

#Calculo datos finales de todos los encuestados
