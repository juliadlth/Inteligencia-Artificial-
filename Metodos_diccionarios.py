#Elimina el diccionario teclado1 entero . De teclado2 elimina las claves 'Categoría' y 'Precio'. Muestra la última clave ('Modelo') que queda en la consola.
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',   #Creamos el diccionario 1 con sus elementos 
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',         #Creamos el diccionario 2 con sus elementos 
	'Precio': '59,99'
}

del teclado1                             #Eliminamos el diccionario teclado 1
del teclado2['Categoría']                #Eliminamos de teclado dos el elemento de categoria 
del teclado2['Precio']                   #Eliminamos de teclado2 el elemento de precio
print(teclado2['Modelo'])                #Eliminamos de teclado2 el elemento de metodo
