def cuandoVacunarse(edad, ocup, personasCasa):
  if edad > 80 or ocup == "Empleado" or personasCasa >= 12 : print("Puede Vacunarse Enseguida")
  elif (edad > 65 and edad <= 80) or ocup == "Contratista" or (personasCasa >= 3 and personasCasa <= 7): print("Se agendara para Julio")
  elif (edad > 40 and edad <= 65) or ocup == "Pensionado" or (personasCasa >= 8 and personasCasa <= 11): print("Se agendara para Septiembre")
  elif (edad < 40 and edad >= 1) or ocup == "Desempleado" or personasCasa == 1 and personasCasa == 2 : print("Se agendara para diciembre")
  else: print("Los datos digitados no son validos en nuestro sistema...")


edad = int(input("¿Edad del paciente? "))
ocup = input("¿Ocupación del Paciente? ")
personasCasa = int(input("¿Número de personas con las que vive? "))

cuandoVacunarse(edad,ocup, personasCasa)

