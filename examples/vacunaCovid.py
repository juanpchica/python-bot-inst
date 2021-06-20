cc = input(':')
edad = input(':')
ocupacion = input(':')
zona = input(':')
cantPersonas = input(':')

numeroPicoCC = cc[-1]

countEnseguida = 0
countJulio = 0
countSeptiembre = 0
countDiciembre = 0

if edad > 80: countEnseguida =+ countEnseguida
elif edad > 65 and edad <=80: countJulio =+ countJulio
elif edad >40 and edad >= 65: countSeptiembre =+ countSeptiembre
elif edad < 40 and edad >=1:  countDiciembre =+ countDiciembre

if ocupacion == 'Empleado': countEnseguida =+ countEnseguida
elif ocupacion == 'Contratista': countJulio =+ countJulio
elif ocupacion == 'Pensionado': countSeptiembre =+ countSeptiembre
elif ocupacion == 'Desempleado' : countDiciembre =+ countDiciembre

if zona == 'Urbana': countEnseguida =+ countEnseguida
elif zona == 'Rural': countJulio =+ countJulio
elif zona == 'Exterior': countSeptiembre =+ countSeptiembre
elif zona == 'Especial' : countDiciembre =+ countDiciembre

if cantPersonas >= 12: countEnseguida =+ countEnseguida
elif cantPersonas >= 3 and cantPersonas <= 7: countJulio =+ countJulio
elif cantPersonas >= 8 and cantPersonas <= 11: countSeptiembre =+ countSeptiembre
elif cantPersonas == 1 or cantPersonas == 2:  countDiciembre =+ countDiciembre

if numeroPicoCC == 0 or numeroPicoCC == 3 or numeroPicoCC == 8: countEnseguida =+ countEnseguida
elif numeroPicoCC == 4 or numeroPicoCC == 6: countJulio =+ countJulio
elif numeroPicoCC == 2 or numeroPicoCC == 9: countSeptiembre =+ countSeptiembre
elif numeroPicoCC == 1 or numeroPicoCC == 5 or numeroPicoCC == 7:  countDiciembre =+ countDiciembre


