#Del listas 
#De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Declaro la lista y sus elementos 
#azul=posicion 1 
#marron=posicion 4 pero al eliminar el azul queda en la 3
#negro=posicion 6 pero al eliminar azul y marron queda en 4
#rosa=posicion -3 
del colores [1]
del colores [3]    #Elimino cada color con su posicion de memoria y el comando "del"
del colores [4]
del colores [-3]

print(colores) #Imprimo la nueva lista

