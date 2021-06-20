cc = input(':')
edad = int(input(':'))
ocupacion = input(':')
zona = input(':')
cantPersonas = int(input(':'))

numeroPicoCC = int(cc[-1])

countEnseguida = 0
countJulio = 0
countSeptiembre = 0
countDiciembre = 0

if edad > 80: countEnseguida =+ countEnseguida
elif edad > 65 and edad <=80: countJulio = countJulio + 1
elif edad >40 and edad >= 65: countSeptiembre = countSeptiembre + 1
elif edad < 40 and edad >=1:  countDiciembre = countDiciembre + 1

if ocupacion == 'Empleado': countEnseguida = countEnseguida + 1
elif ocupacion == 'Contratista': countJulio = countJulio + 1
elif ocupacion == 'Pensionado': countSeptiembre = countSeptiembre + 1
elif ocupacion == 'Desempleado' : countDiciembre = countDiciembre + 1

if zona == 'Urbana': countEnseguida = countEnseguida + 1
elif zona == 'Rural': countJulio = countJulio + 1
elif zona == 'Exterior': countSeptiembre = countSeptiembre + 1
elif zona == 'Especial' : countDiciembre = countDiciembre + 1

if cantPersonas >= 12: countEnseguida = countEnseguida + 1
elif cantPersonas >= 3 and cantPersonas <= 7: countJulio = countJulio + 1
elif cantPersonas >= 8 and cantPersonas <= 11: countSeptiembre = countSeptiembre + 1
elif cantPersonas == 1 or cantPersonas == 2:  countDiciembre = countDiciembre + 1

if numeroPicoCC == 0 or numeroPicoCC == 3 or numeroPicoCC == 8: countEnseguida = countEnseguida + 1
elif numeroPicoCC == 4 or numeroPicoCC == 6: countJulio = countJulio + 1
elif numeroPicoCC == 2 or numeroPicoCC == 9: countSeptiembre = countSeptiembre + 1
elif numeroPicoCC == 1 or numeroPicoCC == 5 or numeroPicoCC == 7:  countDiciembre = countDiciembre + 1

valoresFinales = [countEnseguida,countJulio,countSeptiembre,countDiciembre]

max_value = max(valoresFinales)
max_index = valoresFinales.index(max_value)

if max_index == 0: print("El paciente puede vacunarse Enseguida")
elif max_index == 1: print("Se agendara para Julio")
elif max_index == 2: print("Se agendara para septiembre")
elif max_index == 3: print("Se agendara para diciembre")
