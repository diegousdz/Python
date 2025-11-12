# Lucía Fernández ha tomado recientemente el liderazgo de la firma familiar TecnoHogar Sur S.R.L., la cual ha operado durante años con procedimientos manuales.
# Con el objetivo de optimizar la gestión interna, 
# Lucía ha decidido implementar un sistema informatizado y solicita tu colaboración para desarrollar un programa que cumpla con las siguientes funciones:

# Requisitos del programa:
# 📥 Ingreso y almacenamiento de datos en vectores:

# • Nombre del modelo del producto (en formato textual).

# • Precio unitario (debe ser mayor a cero).

# 🔠 Validaciones especiales:

# • Si el nombre del modelo se ingresa en minúsculas, debe convertirse automáticamente a mayúsculas.✅

# • Si no se ingresan datos, el programa debe emitir un mensaje de aviso.✅
# 🛑 Condición de corte:
# • La carga de productos se interrumpe al ingresar "FIN" como nombre del modelo.✅
# 📊 Procesamiento y visualización:

# • Mostrar todos los productos y sus precios en formato de tabla, utilizando una función.✅

# • Identificar y mostrar el nombre del producto con el precio más bajo.
# • Calcular el precio promedio de todos los productos.
# • Eliminar los productos cuyo precio supere el promedio, junto con sus respectivos valores.
# • Insertar el modelo "PRUEBA" con un precio de 999 inmediatamente después de cada precio par.
# • Ordenar los productos alfabéticamente por nombre, asegurando que los precios acompañen el orden.
# Importante:
# Cada vez que se modifique el contenido de los vectores, se debe mostrar el resultado actualizado con la función creada para mostrar.
#BUBBLE SORT
# DE ESTA FORMA VA A ORDENAR POR PRODCTO, EL PRIMER PARAMETRO QUE LE PASEMOS VA A ORDENAR por ese valor
def ordenar(producto, precio):
    for i in range(len(producto)-1):
        for j in range(i+1, len(producto)):
            if (producto [i]> producto[j]):
                intercambiar

def intercambiar(vec, i, j):
    aux=vec[i]
    vec[i]

def insertar(producto, precio):
    #recorrer el vector
    for i in range(len(producto) -1, -1, -1):
        if (precio[i]%2==0):
                producto.insert(i+1, "PRUEBA")
                precio.insert(i+1, 999)
        


def eliminar(producto, precio, prom):
    #recorrer el vector
    for i in range(len(producto) -1, -1, -1): # METODO ARIEL CASTRO
        if (precio[i]>prom):
            producto.pop(i)
            precio.pop(i)
        
def promedioGenerat(precio):
    acum = 0
    cont = 0

    for i in range(len(precio)):
        acum = acum + precio[i]
        cont = cont + 1

    return acum / cont

def productoPrecioMinimo(vec1):
    posMin = 0
    #SIEMPRE SE USA PARA VAL el vector en posicion 0
    valMin = vec1[0]
    for i in range(len(vec1)):
        #SI el valor de la derecha es menor al de la izquierda
        if(vec1[i]>valMin):
            valMin = vec1[i]
            posMin = i
    return posMin

def mostrarProductos(vec1, vec2):
    for i in range(len(vec1)):
        print(f"El nombre del modelo de producto es {vec1[i]}, y su precio es {vec2[i]}")

def cargaDeProductos(vec1, vec2):

    nombreModeloProducto = str(input("Para cargar productos, ingrese el nombre del modelo de producto o FIN para finalizar la carga: ")).upper()

    while(nombreModeloProducto != "FIN"):

        while(nombreModeloProducto == "" and nombreModeloProducto != "FIN"):
            nombreModeloProducto = str(input("ERROR Para cargar productos, ingrese el nombre del modelo de producto o FIN para finalizar la carga: ")).upper()
        vectorNombreDeProductos.append(nombreModeloProducto)

        precioProducto = int(input("Ingrese el precio del producto en numeros enteros"))
        while(vectorPrecio < 0):
            precioProducto = int(input("Error, Reingrese el precio del producto en numeros enteros"))
        vectorPrecio.append(precioProducto)

        nombreModeloProducto = str(input("Para cargar productos, ingrese el nombre del modelo de producto o FIN para finalizar la carga: ")).upper()

#MAIN
vectorNombreDeProductos = []
vectorPrecio = []

cargaDeProductos(vectorNombreDeProductos, vectorPrecio)

print("Fin del programa")
print(f"Length vector nombre de prodcutos: {len(vectorNombreDeProductos)}")

if(len(vectorNombreDeProductos) > 0):
    mostrarProductos(vectorNombreDeProductos, vectorPrecio)
    posicion_Min = productoPrecioMinimo(vectorPrecio)
    
else:
    print("Error no hay elementos cargados en el systema")
    confirmacionSalirSistema = str(input("Quiere usted salir definitivamente del programa o volver al sistema de carga? Ingrese SI, si quiere volver al sistema de carga o NO para salir: ")).upper()
    
    print(f"message: {confirmacionSalirSistema}")
        
    if(confirmacionSalirSistema == "SI"):
        cargaDeProductos(vectorNombreDeProductos, vectorPrecio)
    else:
        print("Gracias por utilizar Gestión TecnoHogar Sur S.R.L, Vuelva pronto!")
    