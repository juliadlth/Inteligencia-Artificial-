#1.1.1 Conjuntos 
#Declaramos los conjuntos que utilizaremos
GUniverso=set( [1,2,3,4,5,6,7,8,9,10,11,12,13] )                       #Declaramos el conjunto universo
a=set( [1,2,3,4,5,6 ] )                                                #Declaramos el conjunto a
b=set( ["" ] )                                                         #Declaramos el conjunto b y en este caso sera el conjunto vacio 
c=set( [7,8,9,10,11 ] )                                                #Declaramos el conjunto c
d=set( [1,2,3,4,5,6 ] )                                                #Declaramos el conjunto d
Gextension=set( ["5,6,7,8,9" ] )                                       #Declaramos el conjuto de extension
Gcomprension=set( ["x/x es número par mayor que 1 y menor que 10" ] )  #Declaramos el conjunto de comprension

#Conjunto universo y conjunto vacio
  
print("Los elementos del universo son",GUniverso)    #Imprimimos el conjunto universo
print("Los elementos del conjunto vacio son",b)      #Imprimimos el conjunto vacio

#Conjuntos por extension y por comprension 
print("\nLos elementos del conjunto por comprension son",Gcomprension) #Imprimimos el conjunto de compresion
print("Los elementos del conjunto por extension son",Gextension)       #Imprimimos el conjunto de extension 

 #Igualdad de conjuntos 
igualdad = a==b                                            #Generamos la comparacion con el operador"==" y lo guardamos en "igualdad"
print("\nEl conjunto A y B son iguales? ", igualdad)       #Lo imprimimos  da el resultado de "false"porque no son iguales
igualdad = a==d                                            #Generamos la comparacion entre los conjuntos a y d
print("El conjunto A y D son iguales? ", igualdad)         #Lo imprimimos y da como resultado "True" porque son iguales

#Subconjuntos y Superconjuntos 
#Subconjuntos
suba= a.issubset(GUniverso)                                #Hacemos la comparacion utilizando el operador ".issubset()"
print ("\n\nEl conjunto A, es subconjunto del universo? ",suba) #Imprimimos y el dara como resultado "True" porque a si es sub del universo

subb= b.issubset(GUniverso)                                #Hacemos la comparacion utilizando el operador ".issubset()"
print ("El conjunto B, es subconjunto del universo? ",subb)#B no es subconjunto del universo ,entonces sera "False"

subc= c.issubset(GUniverso)                              #Hacemos la comparacion utilizando el operador ".issubset()"
print ("El conjunto C, es subconjunto del universo? ",subc)#Imprimimos y el dara como resultado "True" porque a si es sub del universo

subd= d.issubset(GUniverso)                               #Hacemos la comparacion utilizando el operador ".issubset()"        
print ("El conjunto D, es subconjunto del universo? ",subd)#Imprimimos y el dara como resultado "True" porque a si es sub del universo

subac= a.issubset(c)                                       #Hacemos la comparacion utilizando el operador ".issubset()"
print ("El conjunto A, es subconjunto de C? ",subac)#Imprimimos y el dara como resultado "false" porque a no es sub de c

#Superconjuntos 
super= GUniverso.issuperset(a)                                 #Usamos el operador ".issuperset()" para comparar
print ("\n\nEl universo es un superconjunto del conjunto A? ",super) #Imprimimos el resultado, en este caso es "true"
super = GUniverso.issuperset(b)                              #Usamos el operador para superconjuntos
print ("El universo es un superconjunto del conjunto B? ",super)#Imprimimos el resultado y en esta caso es "False"
super = GUniverso.issuperset(c)                                #Usamos el operador para superconjuntos
print ("El universo es un superconjunto del conjunto C? ",super) #Imprimimos el resultado y en esta caso es "true"

#Unión, Intersección, complemento, diferencia y diferencia simetrica 
#Union 
union = a.union(c)                                          #Utilizamos el operador ".union()" 
print("\n\nLos elementos del conjunto A union C son",union) #Da como resultado la union de ambos conjuntos
#Intersecion 
intersec= a.intersection(c)                                 #Utilizamos el operador ".intersection()"
print("Los elementos del conjunto A interseccion C son",intersec) #Se genera un conjunto con los elementos relacionados
#Diferencia/complemento
difer = a.difference(c)                                     #Utilizamos el operador ".difference()"
print("Los elementos del conjunto A diferencia C son",difer) #Obtenemos un conjunto con la diferencia entre ambos conjuntos 
#Diferencia simetrica 
difersim = GUniverso.symmetric_difference(a)              #Utilizamos el operador ".symmetryc_difference()"    
print("\n\nLa difererencia simetrica del universo y el conjunto A es:", difersim)#Imprimimos el resultado
diferism = GUniverso.symmetric_difference(c)              #Utilizamos el operador ".symmetryc_difference()"
print("La difererencia simetrica del universo y el conjunto B es:", difersim)#Imprimimos el resultado 

#Producto cartesiano
#Relaciones
#Funciones
def get_cart_prd(pools):
  result = [[]]
  for pool in pools:
    result = [x+[y] for x in result for y in pool]
  return result

print("\n\nProducto cartesiano")

mylists = [["a", "b", "c"],
    [1,2,3]]
print (mylists)
print(get_cart_prd(mylists))




