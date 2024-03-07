
#Se declaran diccionarios = Objetos

clienteUno = {
    "id":5,
    "nombre":"edificio1",
    "consumo":200

}

clienteDos = {
    "id":58,
    "nombre":"edificio2",
    "consumo":500

}

#Se declara una lista = arreglo

clientesAsociados=[
    clienteUno,
    clienteDos
]

#Y AHORA QUE HAGO CON ESA LISTA?
#MI OBJETIVO SERA OBTENER LA INFORMACIÓN DE LA LISTA
#RECORRER UNA LISTA O ARREGLO

#print(clientesAsociados)

'''for i in range(2):
    print(clientesAsociados[i]["consumo"])'''

#Programemos un foreach que es un for especializado en recorrer arreglos (listas)

for cliente in clientesAsociados: 
    print(cliente["consumo"])

#ID y despues el valor del consumo y al lado kwh
    
for cliente in clientesAsociados:
    print(cliente["id"], '=>', cliente['consumo'] 'KWH')


#otra forma de hacerlo 
    
   