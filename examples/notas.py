def calculoNotas(notas):
    valorFinal = 0
    notasPorcentaje = [15, 15, 20, 25, 25]
    for n in notas:
        valorFinal += (notas[n] * notasPorcentaje[n]) / 100

    return valorFinal

def logro(nota):
    


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



