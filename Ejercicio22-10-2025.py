# la despensa la figazita quierq llevar el control de las ventas y se registra para ellos los siguientes datos

# numero de ticket
# nombre del comprador mayuscula / upper
# importe abonado que no sea 0
# la carga finaliza con ticket = o / ticket es un dato numerico 
# mostrar el vector 
# ordenar los vector por numero de ticket
# mostrar el vector ordenadfo
# calcular el maximo del os importes
# mostrar el ticket
# -------------

# NOTA: insertar / insert y agregar / append 

# def promedio(importes):
#     for i in range()
    #suma y divide

def eliminar(vec1, vec2, vec3, vec4):
    #for alrevez 
    for i in range(len(vec1)-1, -1, -1):
        if(vec4[i]=="GALLETITA"):
            vec1.pop(i)
            vec2.pop(i)
            vec3.pop(i)
            vec4.pop(i)

def eliminarWhile(vec1, vec2, vec3, vec4):
    i = 0
    while( i < len(vec1)):
        if(vec4[i]=="GALLETITA"):
            vec1.pop(i)
            vec2.pop(i)
            vec3.pop(i)
            vec4.pop(i)
        else:
            i=i+1

def insertar(vec1, vec2, vec3, vec4):
    # dos opciones for inverso o un while 
    # con el while tenemos el problem de que tenemos que estar controlando la i 

    for i in range(len(vec1)-1, -1, -1):
        # con esto me doy cuenta si es part
        if(importe[i]%2 == 0):
            vec1.insert(i+1, 999)
            vec2.insert(i+1, "prueba")
            vec3.insert(i+1,999)
            vec4.inser(i+1, "Prueba")
  

def insertarWhile(vec1, vec2, vec3, vec4):
    i= 0
    while i< len(vec1):
       if(importe[i]%2 == 0):
            vec1.insert(i+1, 999)
            vec2.insert(i+1, "prueba")
            vec3.insert(i+1,999)
            vec4.inser(i+1, "Prueba")
            i=i+1
    i = i+1


def maximo(vectorImport):
    maxi = vectorImport[0]
    posmaxi = 0
    for i in range(len(importe)):
        if(importe[i]>maxi):
            maxi=importe[i]
            posmaxi = i
    return posmaxi

def maxWhile(vectorImport):
    maxi=importe[0]
    pasmaxi = 0
    i= 0
    while(i<len(importe)):
        if(importe[i]>maxi):
            maxi=importe[i]
            posmaxi = i
    return posmaxi

def intercambiar(vector, i, j):
    aux = vector[i]
    vector[i]= vector[j]
    vector[j]= aux

def ordenar(vec1, vec2, vec3, vec4):
    for i in range(len(vec1)-1):
        for j in range(i+1, len(vec1)):
            # ordenar por forma desendeicnete poner <
            if(vec1[i] > vec1[j]):
                intercambiar(vec1, i, j)
                intercambiar(vec2, i, j)
                intercambiar(vec3, i, j)
                intercambiar(vec4, i, j)
            
def mostrar(vec1, vec2, vec3, vec4):
    for i in range(len(vec1)):
        print(vec1[i], vec2[i], vec3[i], vec4[i])
        # formato tabla
        print(f"NRO TICKET {vec1[i]}, IMPORTE {vec2[i]}, NOMBRE DEL COMPRADOR {vec3[i]}, PRODUCTO {vec4[i]}")

def cargar(vec1, vec2, vec3, vec4): 
    nro_ticket = int(input("Ingrese un numero de ticket: "))


    while nro_ticket!= 0:
        vec1.append(nro_ticket)
        nom_comprador = str(input("Ingrese el nombre del comprador: ")).upper()
        vec2.append(nom_comprador)
        imp=int(input("Ingrese el importe: "))
        while(imp<0):
            imp=int(input("Re, ingrese el importe del comprador: "))
        vec3.append(imp)
        nom_prod = str(input("Ingrese el nombre del producto entre las siguientes opciones Galletita, fideos, polenta y pan: ")).upper()
        while(nom_prod!="PAN" and nom_prod!="GALLETITA" and nom_prod!="FIDEOS" and nom_prod!="POLENTA"):
            nom_prod = str(input("ERROR, reingrese el nombre del producto: ")).upper()
        vec4.append(nom_prod)
        nro_ticket = int(input("Ingrese otro numero de ticket o 0 para finalizar: "))

ticket = []
nombre = []
importe = []
producto = []

cargar(ticket, nombre, importe, producto)
if len(ticket)==0:
    print("No hay elementos o ticket cargados")
else:
    mostrar(ticket, nombre, importe, producto)
    # el primer vector que pase como parametro es el que se usa como criterio para ordenar
    # si quiero rodenar por producto, pongo primero el producto
    ordenar(ticket, nombre, importe, producto)
    print("DESPUS DE ORDENAR")
    mostrar(ticket, nombre, importe, producto)
    variablesPosMaxi = maximo(importe)
    print(f"el importe maximo es: {importe[variablesPosMaxi]}, el ticket maximo es {ticket[variablesPosMaxi]}, el producto maximo es {producto[variablesPosMaxi]}, el nombre es {nombre[variablesPosMaxi]}")
    print("Despues de insertar")
    insertar(ticket, nombre, importe, producto)
    mostrar(ticket, nombre, importe, producto)

    eliminar(ticket, nombre, importe, producto)
    print("Despues de eliminar")
    mostrar(ticket, nombre, importe, producto)
