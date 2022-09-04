#Del diccionario teclado2 del capítulo, muestra los elementos Modelo y Precio con presentación en un print(). El resultado será esto en la consola:

teclado1 = {                                             #Declaramos nuestros dicionarios con llaves y con ':' separamos las referencias
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

print('El modelo', teclado2['Modelo'], 'cuesta $', teclado2['Precio']) #Imprimo el modelo y el precio del teclado dos 
