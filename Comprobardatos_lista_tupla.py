colores = input('Introduce un color:\n')      #Le doy la opcion al usuario que ingrese un color 
tupla_colores = ('rosa', 'azul', 'rojo', 'amarillo') #Establezco la tupla y sus elementos 

if colores in tupla_colores[0]:      #Empiezo con mi primer condicional donde si el color que escribio es igual al de la posicion 0
	print('El color rosa está admitido') #Si se cumple , se imprime lo siguiente 
elif colores in tupla_colores[1]:            #Utilizo elif para agregar más condiciones en cada posicion 
	print('El color azul está admitido')     #Se imprime el mensaje si se cumple la condicion
elif colores in tupla_colores[2]:
	print('El color rojo está admitido')
elif colores in tupla_colores[3]:
	print('El color amarillo está admitido')
else:                                   #Si no se cumple el 'if' o algun 'elif' se imprime el 'else'
	print('Color no admitido')          #Se imprime el else 
