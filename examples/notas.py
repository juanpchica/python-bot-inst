
while True:
    print(f'Por favor ingrese la información para el estudiante...')
    identidad = input('Documento Identidad: ')
    nombre = input('Nombre: ')
    grado = int(input('Grado que Cursa: '))
    

    finalizar = print(f'Desea finalizar? Digite Si/No: ')
    if finalizar.upper() == "SI":
        break