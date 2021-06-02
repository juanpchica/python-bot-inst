def cuandoVacunarse(edad, ocup, personasCasa):
  if edad > 80 or ocup == "Empleado" or personasCasa >= 12 : print("Puede Vacunarse Enseguida")
  elif (edad > 65 and edad <= 80) or ocup == "Contratista" or (personasCasa >= 3 and personasCasa <= 7): print("Se agendara para Julio")
  elif (edad > 40 and edad <= 65) or ocup == "Pensionado" or (personasCasa >= 8 and personasCasa <= 11): print("Se agendara para Septiembre")
  elif (edad < 40 and edad >= 1) or ocup == "Desempleado" or personasCasa == 1 and personasCasa == 2 : print("Se agendara para diciembre")

cuandoVacunarse(58, "Contratista", 2)
cuandoVacunarse(81, "Empleado", 5)
cuandoVacunarse(60, "Pensionado", 8)
cuandoVacunarse(25, "Desempleado", 1)