opcion = input('Desea continuar procesando información? Escriba Si/No: ')

cont = 1
encuestado = []
encuestados = []

while opcion.lower() == 'si' and cont <=5:
    print(f'Por favor ingrese la información para el mes #{cont}')
    mes = input('Nombre mes:')
    ingreso = input('Ingreso del mes:')
    personas = input('Cantidad de personas que dependen del ingreso:')

    #Valido margen de pobreza
    if ingreso <= 800000:
        if personas == 1 : margenPobreza = 'Clase media'
        elif personas >= 2 and personas <=5 : margenPobreza = 'Pobre'
        elif personas >= 6 : margenPobreza = 'Muy pobre'



    #guardo datos en una lista
    encuestado.append((mes,int(ingreso),int(personas)))

    cont +=1
    if cont == 5:
        #Calculo datos finales para un encuestado
        for mes in encuestado:
            print(mes[0])



        #Agrego encuestado a lista
        encuestados.append(encuestado)
        opcion = input('Desea continuar procesando información? Escriba Si/No: ')
        if opcion.lower() == 'si' : cont = 1


#Calculo datos finales de todos los encuestados

