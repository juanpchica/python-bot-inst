cc = input(':')
edad = input(':')
ocupacion = input(':')
zona = input(':')
cantPersonas = input(':')

countEnseguida = 0
countJulio = 0
countSeptiembre = 0
countDiciembre = 0

if edad > 80: countEnseguida =+ countEnseguida
elif edad > 65 & edad <=80: countJulio =+ countJulio
elif edad >40 & edad >= 65: countSeptiembre =+ countSeptiembre
else:  countDiciembre =+ countDiciembre
