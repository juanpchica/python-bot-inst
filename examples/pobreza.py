cc = input('Ingrese cc:')
nombre = input('Ingrese Nombre:')

opcion = input('Desea continuar procesando información? Escriba Si/No: ')

cont = 1
meses = []

while opcion.lower() == 'si' and cont <=5:
    print(f'Por favor ingrese la información para el mes #{cont}')
    mesNombre = input('Nombre mes:')
    ingreso = input('Ingreso del mes:')
    personas = input('Cantidad de personas que dependen del ingreso:')

    #guardo datos en una lista
    meses.append((mesNombre,int(ingreso),int(personas)))

    cont +=1

for mes in meses:
    print(mes[0])
