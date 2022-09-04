
x = 0 #Le doy un valor inicial a mi x

while x <= 30: #Creo mi while cuando x es menos o igual que 30
	x += 1  # incrementos de 1

	
	if x == 4 or x == 6 or x == 10:  #Declaro mi if para poder saltar esos valores de mi bucle
		print('Se saltó el valor ', x, ' de x') #Ecribo un mensaje en el 4,6,10
		continue          #El continue para que continue despues de los valores restringuidos

	
	if x == 15:  #declaro mi if para igualarlo en 15
		print('Se rompió la ejecución del bucle cuando x valía: ', x) #Escribo el mensaje en el 15 
		break  #Rompo mi bucle 

	print("El valor del bucle es: " + str(x))# imprime los resultados que no se corresponden a ninguno de los if