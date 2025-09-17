#Una base espacial está recibiendo a los nuevos 5 tripulantes para una misión interplanetaria. (Ya me da la cantidad))
# un input para el nombre y un input para la edad
# while 

# 1 tenemos un for y en el for tenemos 2 input.
# sabemos que una de esas 2 variables las validamos con while 
# si pone 15 tiene que decir error, no tienes que ingresar una edad  validad. ingrese entre esos parametros
# tnemos maximo y minimos (tomamos el primer valor leido y luego comparamos con el resto) 
# promedio es la suma de todos / la cantidad. Esto esta afuera del ciclo
# contar cuantos tripulantes tienen edades par o impar 
# si es par. Ponemos modulo de 2 == 0. Si es par, cuento ELSE cuento impares.
# sie s multiplo de 7. 

# multiplo de 7, edad modulo 7 == 0 sumar. 

# edad % 2 != 0 and edad > 30 

# edad == 42
# for hasta 3 y adentro leo codigo = int("


cantidadNuevosTripulantes = int(3)
tripulanteMasJoven = int(0)
tripulanteMasVeterano = int(0)
calculoPromedioEdad = int(0)
contadorCantidadTripulatesEdadPar = int(0)
contadorCantidadTripulatesEdadImpar = int(0)
acumuladorEdadesMayoresTreintaEImpar = int(1)

for i in range(cantidadNuevosTripulantes):
      
    nombreTripulante = str(input("Por favor ingresar su Nombre")).upper()
    print(f"Su nombre es: {nombreTripulante}")

    # pre condicion 
    edadTripulante = int(input("Por favor ingresar su Edad"))
    print(f"Su edad es: {edadTripulante}")

    calculoPromedioEdad = calculoPromedioEdad  + edadTripulante 
    esUnaEdadValida = int(0)

    while(edadTripulante < 18 or edadTripulante > 65 ): 
        nuevaEdad = int(input(f"Ingreso una edad invalida, tiene que ser una edad entre 18 y 65.\n Ingrese su nueva edad: "))
        print(f"Su nueva edad es {nuevaEdad}")
        if(nuevaEdad != edadTripulante): 
            edadTripulante = nuevaEdad
        else:
            print("ingreso un una edad igual a la anterior")

    if (i == 0):
        tripulanteMasJoven  = edadTripulante 
    
    if(edadTripulante >  tripulanteMasVeterano):
        tripulanteMasVeterano = edadTripulante 


    if(edadTripulante <  tripulanteMasJoven):
        tripulanteMasJoven = edadTripulante

    if(edadTripulante % 2 == 0):
        #Es par
        contadorCantidadTripulatesEdadPar = contadorCantidadTripulatesEdadPar + 1
    else:
        #es inpar
        contadorCantidadTripulatesEdadImpar = contadorCantidadTripulatesEdadImpar + 1
        if(edadTripulante > 30):
            acumuladorEdadesMayoresTreintaEImpar = acumuladorEdadesMayoresTreintaEImpar * edadTripulante 
            print(f"La energía total que aportan los tripulantes al sistema es: {acumuladorEdadesMayoresTreintaEImpar }")
    
    if(edadTripulante == 42):
        codigoSecretoUno = int(input("ingresar un numero random y que sea secreto: "))
        codigoSecretoDos = int(input("ingresar otro numero random y que sea secreto: "))
        codigoSecretoTres = int(input("ingresar finalmente otro numero random y que sea secreto: "))
        totalSumaCodigosSecretos = int(codigoSecretoUno + codigoSecretoDos + codigoSecretoTres)
    else: 
        print("Ningún tripulante con edad 42 fue detectado.")
    
print(f"Edad mas joven: {tripulanteMasJoven}")
print(f"Edad mas veterano: {tripulanteMasVeterano}")
print(f"Promedio edad: {calculoPromedioEdad  /  cantidadNuevosTripulantes }")

