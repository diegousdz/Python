#bubble sort
# cada numero esta en una posicion. 

# se intercambian posiciones para ordenarse

# se ordenaron en pareja

# se ordenaron por pareja, yo soy mas chico, vos sos mas grande y vas a la derecha

# buca a la companera,si es mas chico si es mas chico se acomoda a la izquierda 

# la siguiente pareja si es mas grande se acomoda a la derecha si es mas pequeno quien inicio va a la izquierda 

# funcion ordernar se usa for (1 o +) como maximo para comparacion, y despues de ordena en el for 

# nuestro bailarin principal va a ir comparando y si encuentra alguno va a ir intercambiando 

# el bailarin de la izquierda agarraba el bailarin de la derecha

# para hacer el bubble sor tenemos, comparacion luego ciclos de repeticion con 2 for y luego un intercambio 

# el intercambio de la primera y ultima posicion 

# https://pythontutor.com/render.html#mode=display

array = [0, 9, 8, 5, 2, 3, 1, 4, 6, 7]
arraTwo = [1, 7, 8, 5, 2, 3, 0, 4, 6, 9]
arrayThree = ["Mike", "Ariel", "Arjona", "Miguel", "Andres", "Diego", "Pedro", "Liza", "Barbara", "Ezequiel"]

def mostra(vecMostrar):
    #muestra el array cargado en memoria
    print(vecMostrar)

def baile(vectorU, posI, posJ):
    aux = vectorU[posI]
    vectorU[posI] = vectorU[posJ]
    vectorU[posJ] = aux

def bubbleSort(arrayInput, arraTwo, arrayThree):
    for i in range(len(arrayInput)-1):
        numeroComparaciones = i + 1
     
        for j in range( i+1, len(arrayInput)):
            numeroComparacionesDos = j
    
            #se comparan entre ellos, yo voy a la izquierda y vos a la derecha
            # esto es de menor a mayor si quieren que sea de mayor a menor usa el < 
            if(arrayInput[i] > arrayInput[j]):
                #intercambio - necesitamos un auxiliar 
                baile(arrayInput, i, j)
                baile(arraTwo, i, j)
                baile(arrayThree, i, j)
    
    print(numeroComparaciones)
    print(numeroComparacionesDos)
   # no hace falta que use el return porque trabaja con la memoria
    # return

#main
mostra(arrayThree)
bubbleSort(array, arraTwo, arrayThree)

mostra(array)
mostra(arraTwo)
mostra(arrayThree)

