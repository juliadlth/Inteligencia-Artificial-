#Parte 1
#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') #Es un total de 4 argumentos
colores('lila', 'negro', 'rojo')             #Es un total de 3 argumentos
colores('rosa')                              #Un total de 1 argumento
colores('marrón', 'naranja')                 #Un total de 2 argumentos 
#Parte 2
#Completa el siguiente fragmento de código
def color(*args):        #Declaramos la funcion
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.') #Imprimimos los argumentos

color('verde', 'rosa') #Creo los colores y su posicion 

#Parte 3
#Crea una función que realice la suma de cinco números utilizando solo *args. Debes imprimir el resultado en la consola. La suma no se realizará directamente sobre el print().
def suma(*args):       #Declaramos la funcion
	resultado = args[0] + args[1] + args[2] + args[3] + args[4] #Declaramos resultado para hacer la suma aparte
	print('El resultado de sumar estos cinco números es:', resultado) #imprimimos el resultado

suma(10, 20, 15, 5, 700, 41) #Declaramos los valores que se van a tomar 
