#Calculo nota segun porcentajes dados
def calculoNotas(notas):
    valorFinal = 0
    notasPorcentaje = [0.1, 0.1, 0.2, 0.25, 0.25]
    val = 0
    for n in notas:
        valorFinal += (n * notasPorcentaje[val])
        val += 1
    return valorFinal

#Calculo el logro por nota
def Obtenerlogro(nota):
    valorLogro = ""
    if nota >= 0 and nota < 4: valorLogro = "Malo"
    elif nota >= 4 and nota < 6: valorLogro = "Regular"
    elif nota >= 6 and nota < 8: valorLogro = "Bueno"
    elif nota >= 8 and nota < 9: valorLogro = "Sobresaliente"
    elif nota >= 9 and nota <= 10: valorLogro = "Excelente"
    else: valorLogro = ""
    return valorLogro

promedioGrado0 = 0
promedioGrado1 = 0
promedioGrado2 = 0
promedioGrado3 = 0
promedioGrado4 = 0
promedioGrado5 = 0
promedioGrado6 = 0
promedioGrado7 = 0
promedioGrado8 = 0
promedioGrado9 = 0
promedioGrado10 = 0
promedioGrado11 = 0
ngrado0 = 0
ngrado1 = 0
ngrado2 = 0
ngrado3 = 0
ngrado4 = 0
ngrado5 = 0
ngrado6 = 0
ngrado7 = 0
ngrado8 = 0
ngrado9 = 0
ngrado10 = 0
ngrado11 = 0
estudiantes = []
while True:
    notas = []
    print(f'Por favor ingrese la información para el estudiante...')
    while True:
        try:
            identidad = int(input('Documento Identidad: '))
        except ValueError:
            print("El valor digitado no es un numero, escriba un numero")
            continue
        if type(identidad) == int:
            break
    nombre = str(input('Nombre: '))
    for n in nombre:
        for i in "0123456789":
            if n == i:
                print("Datos ingresados no validos, escriba su nombre: ")
                nombre = str(input('Nombre: '))
                continue
    while True:
        try:
            grado = int(input('Grado que cursa: '))
        except ValueError:
            print("El valor digitado no es un numero, escriba un numero")
            continue
        if grado > 11 or grado < 0:
            print("El grado ingresado no es valido, ingrese un grado valido: ")
            continue
        if type(grado) == int:
            break


    nota1 = float(input('Primer Nota: '))
    while nota1 > 10 or nota1 < 0:
        print("Valor no valido,digite un valor entre cero y diez")
        nota1 = float(input('Primer Nota: '))
    notas.append(nota1)
    nota2 = float(input('Segunda Nota: '))
    while nota2 > 10 or nota2 < 0:
        print("Valor no valido,digite un valor entre cero y diez")
        nota2 = float(input('Segunda Nota: '))
    notas.append(nota2)
    nota3 = float(input('Tercera Nota: '))
    while nota3 > 10 or nota3 < 0:
        print("Valor no valido,digite un valor entre cero y diez")
        nota3 = float(input('Tercera Nota: '))
    notas.append(nota3)
    nota4 = float(input('Cuarta Nota: '))
    while nota4 > 10 or nota4 < 0:
        print("Valor no valido,digite un valor entre cero y diez")
        nota4 = float(input('Cuarta Nota: '))
    notas.append(nota4)
    nota5 = float(input('Quinta Nota: '))
    while nota5 > 10 or nota5 < 0:
        print("Valor no valido,digite un valor entre cero y diez")
        nota5 = float(input('Quinta Nota: '))
    notas.append(nota5)

    valorNota = calculoNotas(notas)

    #Calculo logro
    logro  = Obtenerlogro(valorNota)

    comentario = "Vamos por Buen Camino"

    #Valido si es necesario o no agregar un comentario
    if logro == 'Malo' or logro == 'Regular':
        comentario = input('Agregar un comentario de refuerzo para este estudiante: ')


    estudiante = (identidad,nombre,grado,notas,valorNota,logro,comentario)
    estudiantes.append(estudiante)


    finalizar = input('Si desea continuar presione enter, si no escriba la palabra NO ')
    if grado == 0:
        ngrado0 += 1
        promedioGrado0 += valorNota
    elif grado == 1:
        ngrado1 += 1
        promedioGrado1 += valorNota
    elif grado == 2:
        ngrado2 += 1
        promedioGrado2 += valorNota
    elif grado == 3:
        ngrado3 += 1
        promedioGrado3 += valorNota
    elif grado == 4:
        ngrado4 += 1
        promedioGrado4 += valorNota
    elif grado == 5:
        ngrado5 += 1
        promedioGrado5 += valorNota
    elif grado == 6:
        ngrado6 += 1
        promedioGrado6 += valorNota
    elif grado == 7:
        ngrado7 += 1
        promedioGrado7 += valorNota
    elif grado == 8:
        ngrado8 += 1
        promedioGrado8 += valorNota
    elif grado == 9:
        ngrado9 += 1
        promedioGrado9 += valorNota
    elif grado == 10:
        ngrado10 += 1
        promedioGrado10 += valorNota
    elif grado == 11:
        ngrado11 += 1
        promedioGrado11 += valorNota

    if finalizar.lower() == "no":
        if ngrado0 == 0:
            ngrado0 = 1
        promedioGrado0 = promedioGrado0 / ngrado0
        if ngrado1 == 0:
            ngrado1 = 1
        promedioGrado1 = promedioGrado1 / ngrado1
        if ngrado2 == 0:
            ngrado2 = 1
        promedioGrado2 = promedioGrado2 / ngrado2
        if ngrado3 == 0:
            ngrado3 = 1
        promedioGrado3 = promedioGrado3 / ngrado3
        if ngrado4 == 0:
            ngrado4 = 1
        promedioGrado4 = promedioGrado4 / ngrado4
        if ngrado5 == 0:
            ngrado5 = 1
        promedioGrado5 = promedioGrado5 / ngrado5
        if ngrado6 == 0:
            ngrado6 = 1
        promedioGrado6 = promedioGrado6 / ngrado6
        if ngrado7 == 0:
            ngrado7 = 1
        promedioGrado7 = promedioGrado7 / ngrado7
        if ngrado8 == 0:
            ngrado8 = 1
        promedioGrado8 = promedioGrado8 / ngrado8
        if ngrado9 == 0:
            ngrado9 = 1
        promedioGrado9 = promedioGrado9 / ngrado9
        if ngrado10 == 0:
            ngrado10 = 1
        promedioGrado10 = promedioGrado10 / ngrado10
        if ngrado11 == 0:
            ngrado11 = 1
        promedioGrado11 = promedioGrado11 / ngrado11
        break

#Recorro todos lo estudiantes agregados
numero = 1
for estu in estudiantes:
    print(f'Estudiante #{numero} ')
    print(f'Nombre: {estu[1]}')
    print(f'Promedio: {estu[4]}')
    print(f'Logro: {estu[5]}')
    print(f'Comentario: {estu[6]}')
    numero += 1
if promedioGrado0 != 0:
    print(f"La nota promedio del grado cero es: {promedioGrado0}")
    logro0 = Obtenerlogro(promedioGrado0)
    print(logro0)
if promedioGrado1 != 0:
    print(f"La nota promedio del grado uno es: {promedioGrado1}")
    logro1 = Obtenerlogro(promedioGrado1)
    print(logro1)
if promedioGrado2 != 0:
    print(f"La nota promedio del grado dos es: {promedioGrado2}")
    logro2 = Obtenerlogro(promedioGrado2)
    print(logro2)
if promedioGrado3 != 0:
    print(f"La nota promedio del grado tres es: {promedioGrado3}")
    logro3 = Obtenerlogro(promedioGrado3)
    print(logro3)
if promedioGrado4 != 0:
    print(f"La nota promedio del grado cuatro es: {promedioGrado4}")
    logro4 = Obtenerlogro(promedioGrado4)
    print(logro4)
if promedioGrado5 != 0:
    print(f"La nota promedio del grado cinco es: {promedioGrado5}")
    logro5 = Obtenerlogro(promedioGrado5)
    print(logro5)
if promedioGrado6 != 0:
    print(f"La nota promedio del grado seis es: {promedioGrado6}")
    logro6 = Obtenerlogro(promedioGrado6)
    print(logro6)
if promedioGrado7 != 0:
    print(f"La nota promedio del grado ciete es: {promedioGrado7}")
    logro7 = Obtenerlogro(promedioGrado7)
    print(logro7)
if promedioGrado8 != 0:
    print(f"La nota promedio del grado ocho es: {promedioGrado8}")
    logro8 = Obtenerlogro(promedioGrado8)
    print(logro8)
if promedioGrado9 != 0:
    print(f"La nota promedio del grado nueve es: {promedioGrado9}")
    logro9 = Obtenerlogro(promedioGrado9)
    print(logro9)
if promedioGrado10 != 0:
    print(f"La nota promedio del grado diez es: {promedioGrado10}")
    logro10 = Obtenerlogro(promedioGrado10)
    print(logro10)
if promedioGrado11 != 0:
    print(f"La nota promedio del grado once es: {promedioGrado11}")
    logro11 = Obtenerlogro(promedioGrado11)
    print(logro11)