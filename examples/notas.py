#Calculo nota segun porcentajes dados
def calculoNotas(notas):
    valorFinal = 0
    notasPorcentaje = [0.1, 0.1, 0.2, 0.25, 0.25]
    val = 0
    for n in notas:
        valorFinal += n * notasPorcentaje[val]
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

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

estudiantes = []
while True:
    notas = []
    print(f'Por favor ingrese la información para el estudiante...')

    #Valido que numero de identidad sea numerico
    while True:
        try:
            identidad = int(input('Documento Identidad: '))
        except ValueError:
            print("El valor digitado no es un numero, escriba un numero")
            continue
        if type(identidad) == int:
            break

    #Valido que nombre no contenga numeros
    nombre = str(input('Nombre: '))
    hasNumber = hasNumbers(nombre)
    while hasNumber:
        print("Datos ingresados no validos, escriba su nombre: ")
        nombre = str(input('Nombre: '))
        hasNumber = hasNumbers(nombre)

    #Valido grado ingresado para estudiante
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
    
    notas.append(float(input('Primer Nota: ')))
    notas.append(float(input('Segunda Nota: ')))
    notas.append(float(input('Tercer Nota: ')))
    notas.append(float(input('Cuarta Nota: ')))
    notas.append(float(input('Quinta Nota: ')))

    #Calculo el valor de las notas
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
    if finalizar.lower() == "no":
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