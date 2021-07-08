import json

#Cargo archivo json con escalas
f = open("escalas.json", "r")
content = f.read()
escalasDictionary = json.loads(content)
f.close()

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

    #Recorro escalas y doy logro de acuerdo a nota
    for escala in escalasDictionary:
        if nota >= escalasDictionary[escala]["inferior"] and nota < escalasDictionary[escala]["superior"]:
            valorLogro = escalasDictionary[escala]["escala"]
            break
        elif nota == 10: valorLogro = escalasDictionary["3"]["escala"]

    return valorLogro

#Detecto si string tiene numeros
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#Calculo promedio segun lista
def promedio(lista):
    prom = sum(lista) / len(lista)
    return prom


estudiantes = []
gradosIngresados = []

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

    #Valido tipo de notas que sean decimal o numero entero
    contNota = 1
    while contNota <= 5:
        try:
            nota = float(input(f'Ingrese Nota #{contNota}: '))
        except ValueError:
            print("La nota ingresada no tiene un valor valido, intenta nuevamente...")
            continue
        if nota > 10 or nota < 0:
            print("Valor no valido,digite una nota entre cero y diez...")
            continue
        elif type(nota) == float:
            notas.append(nota)
            contNota += 1

    #Calculo el valor de las notas
    valorNota = calculoNotas(notas)

    #Calculo logro
    logro  = Obtenerlogro(valorNota)

    comentario = "Vamos por Buen Camino"

    #Valido si es necesario o no agregar un comentario
    if logro == 'Malo' or logro == 'Regular':
        comentario = input('Agregar un comentario de refuerzo para este estudiante: ')

    gradosIngresados.append(grado)
    estudiante = (identidad,nombre,grado,notas,valorNota,logro,comentario)
    estudiantes.append(estudiante)


    finalizar = input('Si desea continuar presione enter, si no escriba la palabra NO ')
    if finalizar.lower() == "no":
        break


#Detecto grados ingresados sin repetir
grados = set(gradosIngresados)
grados = list(grados)

#Recorro todos lo estudiantes agregados
numero = 1
dict_grado_prom = {};

for estu in estudiantes:

    #Agrego datos en dictionary de grados, para calculo de promedio por grado
    if estu[2] in dict_grado_prom:
        dict_grado_prom[estu[2]].append(estu[4])
    else:
        dict_grado_prom[estu[2]] = [estu[4]]

    print(f'Estudiante #{numero} ')
    print(f'Nombre: {estu[1]}')
    print(f'Promedio: {estu[4]}')
    print(f'Logro: {estu[5]}')
    print(f'Comentario: {estu[6]}')
    numero += 1

#Muestro promedio por grados
for key in dict_grado_prom:
    promedioGrado = promedio(dict_grado_prom[key])
    print(f'El promedio del grado {key} es {round(promedioGrado,2)} y el logro es: {Obtenerlogro(promedioGrado)}')