#Calculo nota segun porcentajes dados
def calculoNotas(notas):
    valorFinal = 0
    notasPorcentaje = [15, 15, 20, 25, 25]
    for n in notas:
        valorFinal += (notas[n] * notasPorcentaje[n]) / 100

    return valorFinal

#Calculo el logro por nota
def logro(nota):
    valorLogro = ""
    if nota >= 0 and nota < 4: valorLogro = "Malo"
    elif nota >= 4 and nota < 6: valorLogro = "Regular"
    elif nota >= 6 and nota < 8: valorLogro = "Bueno"
    elif nota >= 8 and nota < 9: valorLogro = "Sobresaliente"
    elif nota >= 9 and nota <= 10: valorLogro = "Excelente"
    else: valorLogro = ""
    return valorLogro

notas = []
estudiantes = []
while True:
    print(f'Por favor ingrese la información para el estudiante...')
    identidad = input('Documento Identidad: ')
    nombre = input('Nombre: ')
    grado = int(input('Grado que Cursa: '))
    notas.append(int(input('Primer Nota: ')))
    notas.append(int(input('Segunda Nota: ')))
    notas.append(int(input('Tercer Nota: ')))
    notas.append(int(input('Cuarta Nota: ')))
    notas.append(int(input('Quinta Nota: ')))

    #Calculo el valor de las notas
    valorNota = calculoNotas(notas)

    estudiante = (identidad,nombre,grado,notas,valorNota)
    estudiantes.append(estudiante)


    finalizar = print(f'Si desea continuar presione enter, si no escriba la palabra NO ')
    if finalizar.upper() == "NO":
        break



