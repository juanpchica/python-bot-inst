def sumIntPares():
    sum = 0
    for x in range(2,100,2):
        sum += x
    print(sum)

#sumIntPares()

######################################################

def factorial(n):
    fact = 1
    if n < 0: print('Factorial no existe en numeros negativos')
    else:
        for x in range(1, n+1):
            fact = fact*x
        print(fact)

#factorial(10)

######################################################

def num15y200():
    for x in range(15,205,5):
        print(x)

#num15y200()

######################################################

def sumDatosUsuario(cant):
    num = 0
    for x in range(cant):
        num += int(input("Ingrese un nuevo numero: "))

    print("La suma total es: " + str(num))


def preguntarUsuarioCant():
    cant = int(input('Ingrese cantidad de veces: '))
    sumDatosUsuario(cant)

#preguntarUsuarioCant()

######################################################

def ingresarFrase():
    voc=0
    frase = str(input('Ingrese una frase: '))
    for caracter in frase:
        if caracter in "aeiouAEIOU":
            voc = voc+1

    print("La frase contiene "+ str(voc) +" vocales")

#ingresarFrase()

######################################################

def sumMultiplos3():
    sum = 0
    for n in range(1,100):
        if(n % 3 == 0):
            sum += n
    print("La suma de los numeros multiplos de 3 entre 0 y 100 es "+str(sum))

sumMultiplos3()