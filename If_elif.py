#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.


edad = int(input('¿Cuál es tu edad?\n')) #se pregunta la edad para que el usuario pueda ingresar su edad
if edad <= 0:                            #Se establece la primera condicion donde nadie puede tener 0 años o menos
	print('Nadie puede tener esa edad.') #Si el usuario ingresa '0' o menos ,se imprime en consola este mensaje
elif edad <= 1 and edad < 18:            #Se establece una segunda condicion donde si el usuario tiene 1-18 años
	print('Eres menor de edad.')         #Se imprime este mensaje en consola 
elif edad == 18 and edad <= 45:           #Estblezco la condicion donde si tienes entre 18 y 45 años 
	print('Eres mayor de edad.')         #Se imprime este mensaje en consola
elif edad <= 100:                        #Se establece la condicion donde si se tiene menos o 100 años 
	print('Eres mayor de edad.')         #Se imprime el siguiente mensaje 
elif edad > 100 and edad <= 120:         #Se establece la condicion con elif si se tiene entre 100-120
	print('Felicidades has tenido una larga vida ') #Se imprime este mensaje
else:                                     #Si no se cumple ninguna de las condiciones anteriores
	print('Edad no válida.')             #Se imprime este mensaje 
