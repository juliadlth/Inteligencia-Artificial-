#Elimina de la siguiente lista los elementos 'azul' y 'blanco'
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Declaro la lista con sus elementos 
#azul=posicion 1  
#Blanco=posicion -2
col1=colores.pop(1)  #Utilizo '.pop()'para eliminar el color azul y guardarlo en la variable col1
col2=colores.pop(-2) #Utilizo '.pop()'para eliminar el color azul y guardarlo en la variable col1
lista2=[col1,col2]   #Creo una nueva lista con las nuevas variables de los colores
print(lista2)        #Imprimo mi lista nueva


