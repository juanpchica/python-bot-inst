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

    estudiante = (identidad,nombre,grado,notas)
    estudiantes.append(estudiante)


    finalizar = print(f'Si desea continuar presione enter, si no escriba la palabra NO ')
    if finalizar.upper() == "NO":
        break