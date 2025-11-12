# Desarrollar un programa en Python que permita gestionar un inventario de libros . El sistema debe permitir al usuario ingresar información sobre distintos libros, incluyendo su nombre, precio y cantidad deseada. El ingreso de datos finaliza cuando el usuario introduce la palabra clave "FIN" como nombre del libro.

# Una vez ingresados los datos, el programa debe realizar las siguientes operaciones:

# 1. Mostrar los datos ingresados: Título, precio y cantidad de cada libro en formato tabla.

# 2. Calcular el promedio de precios desde la mitad del vector de precios hasta el final.

# 3. Identificar el libro con mayor cantidad y mostrar su información.

# 4. Determinar el libro con menor cantidad de ejemplares, siempre que su precio sea mayor a $50.

# 5. Eliminar libros cuya cantidad sea impar y mayor a 50.

# 6. Reemplazar libros cuya cantidad esté entre 15 y 35 por valores Libro="pepe",precio=999,cantidad=999.

# 7. Insertar un nuevo libro en la mitad de las listas con valores fijos.

# 8. Insertar un después de cada libro cuyo precio sea impar Libro="INSERTAR",precio=999,cantidad=999.

# 9. Ordenar alfabéticamente los libros por título, manteniendo la coherencia entre las listas.

# 10. Intercambiar el primer y último elemento de cada lista.

# Cada operación debe ser reflejada en pantalla mostrando el estado actualizado de las listas. Si no se ingresan datos, el programa debe notificarlo al usuario.


def cargar(vec1, vec2, vec3):
    tempNombreLibro = str(input("Ingresar nombre del libro o fin para finalizar la carga: ")).upper()
    while(tempNombreLibro != "FIN"):
        vec1.append(tempNombreLibro)
        tempPrecioLibro = int(input("Ingresar un precio: "))
        while(tempPrecioLibro <= 0):
            tempPrecioLibro = int(input("ERROR, reingresar un precio: "))
        vec2.append(tempPrecioLibro)
        tempCantidadLibros = int(input("Ingresar una cantidad de libros: "))
        while(tempCantidadLibros <= 0):
            tempCantidadLibros = int(input("Error, reingresar una cantidad de libros: "))
        vec3.append(tempCantidadLibros)
        tempNombreLibro = str(input("Ingresar nombre del libro o fin para finalizar la carga: ")).upper()

# Mostrar los datos ingresados: Título, precio y cantidad de cada libro en formato tabla.
def mostrar(vec1, vec2, vec3):
	for i in range(len(vec1)):
		print(f"Titulo libro: {vec1[i]}, Precio libro: {vec2[i]}, Cantidad libros: {vec3[i]}")

def calcularPromedio(vector):
    cont = 0
    acum = 0
    mitad = len(vector)//2
    inicio = 0 
    final = 0
    paso = 0
    for i in range(mitad, len(vector), 1):
        cont+= 1
        acum+= vector[i]
    return acum/cont

def mayorCantidad(vector):
     # esto es siempre igual 
    posMax = 0 
     # es el que utilizamos luego para comparar con el resto de valores
    maximo = vector[0]

    for i in range(len(vector)):
        if(vector[i]>maximo):
            maximo = vector[i]
            posMax = i
    
    return posMax

def menorCantidadEjemplaresMayoresA50Pesos(vector2, vector3):
    posmin = 0
    minimo = vector2[0]
    for i in range (len(vector2)):
         if(vector2[i]<minimo):
              if(vector3[i]>50):
                   minimo = vector2[i]
                   posmin = i
    return posmin


def eliminar(vec1, vec2, vec3):
    for i in range(len(vec1)-1, -1, -1):
        if(vec2[i]%2!=0 and vec2[i]>50):
                vec1.pop(i)
                vec2.pop(i)
                vec3.pop(i)

def remplazar(vec1, vec2, vec3):
    for i in range(len(vec1)):
        if(vec2[i]>15 and vec2[i]<35):
             vec1[i]="PEPE"
             vec2[i]=999
             vec3[i]=999


# insertar un nuevo libro en la mitad de las listas con valor fijos 
def insertarEnLaMitad(vec1, vec2, vec3):
    vec1.insert(len(vec1)//2,"NUEVO LIBRO")
    vec2.inser(len(vec2)//2, 999)
    vec3.inser(len(vec3)//2, 999)

def insertartDespuesDe(vec1, vec2, vec3):
    for i in range(len(vec1)-1, -1, -1):
        if(vec2[i]>2!=0):
            vec1.insert(i+1, "INSERTAR")
            vec2.insert(i+1, 999)
            vec3.insert(i+1, 999)
#ordenar es siempre igual
def ordenar(vec1, vec2, vec3):
    for i in range(len(vec1)-1):
         for j in range(i +1, len(vec1)):
              if(vec1[i])
   
        

# MAIN 

nombreLibro = []
precioLibro = []
cantidadLibros = []

cargar(nombreLibro, precioLibro, cantidadLibros)
if(len(nombreLibro) > 0):
    mostrar(nombreLibro, precioLibro, cantidadLibros)
    prom = calcularPromedio(precioLibro)
    print(f"El promedio de precios es: {prom}")
    print(f"La cantidad de libros maximo es {cantidadLibros[mayorCantidad(cantidadLibros)]}")
    print(f"La camtodad de libros minimos mayor a 50 pesos es {cantidadLibros[menorCantidadEjemplaresMayoresA50Pesos(cantidadLibros,precioLibro)]}")
    eliminar(nombreLibro, precioLibro, cantidadLibros)
    print("DESPUES DE ELIMNAR QUEDA: ")
    mostrar(nombreLibro, precioLibro, cantidadLibros)
    remplazar(nombreLibro, precioLibro, cantidadLibros)
    print("DESPUES DE REMPLAZAR QUEDA: ")
    insertartDespuesDe(nombreLibro, precioLibro, cantidadLibros)

else: 
    print("No hay libros")