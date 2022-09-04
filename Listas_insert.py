#Añade a la siguiente lista los colores 'magenta' y 'turquesa' utilizando insert()
#posicionar 'magenta' en la posición siguiente a la de 'lila' y 'turquesa' en la penúltima posición. Deberás hacer esto utilizando posiciones de lista negativas.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Declaro la lista y sus elementos

#magenta=-4 por ser una posicion siguiente al lila
#turquesa=-1 por ser la penultima posicion 

colores.insert(-4,'magenta') #Utilizo '.insert()'para añador un nuevo elemento en la posicion requerida
colores.insert(-1,'turquesa')#Primero establezco la posicion y despues el elemento
print(colores) #Imprimo la nueva lista 
