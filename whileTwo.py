numerosDeEjemplos = int(3)
pickerEjemplo = int(input(f"ingrese que ejercicio quiere probar, elija del 0 al {numerosDeEjemplos}: "))

if(pickerEjemplo == 0):
    for i in range (0,5, 1):
        print(i)
elif(pickerEjemplo == 1):
    for i in range(5, -1, -1):
        print(i)
elif(pickerEjemplo == 2):
    #pedir salarios a todos los empleados
    numeroDeEmpleados = int(input("Ingrese el numero de empleados de la UP: "));
    print(f"El numero de empleados es: {numeroDeEmpleados}")

    totalSalarios = int(0)

    for i in range(0,numeroDeEmpleados, 1):
        salarioActualEmpleado = int(input(f"Estimado empleado de la UP con ID {i}, por favor ingresar su salario: "))
        totalSalarios = totalSalarios + salarioActualEmpleado
        print(f"El total de los salarios es: {totalSalarios}")

elif(pickerEjemplo == 3):

    contadorIngresosDeSalarios = int(0)
    numeroDeEmpleados = int(input("Buen dia estimado, por favor ingresar el numero de empleados: "))

    totalSalarios = int(0)
    totalEdades = int(0)
    operacionEdadesSalarios = int(0)
    contador = int(0)
    j = 0
        
    while j < numeroDeEmpleados:
        contador = contador + 1
        #ingresar Nombre
        nombreEmpleado = str(input("Por favor ingresar su nombre completo: "))
        #ingresar edad
        edadEmpleado = int(input("Por favor ingresar su edad: ")) 
        #si la edad es menor a 18, no pedir salario
        if(edadEmpleado >= 18):
            #ingresar salario
            salarioActualEmpleado = int(input(f"Estimado empleado {nombreEmpleado}, por favor ingresar su salario con numeros enteros: "))
            #contar cantidad de ingresos de salario
            contadorIngresosDeSalarios = contadorIngresosDeSalarios + 1
        elif(edadEmpleado < 18):
            print("Usted no tiene edad suficiente para trabajar")  
            salarioActualEmpleado = int(0)
        else:
            print("edad no reconocida")
            salarioActualEmpleado = int(0)
        
        #sumar todas las edades
        totalEdades = totalEdades + edadEmpleado
        print(f"El total de las edades hasta ahora es: {totalEdades}")
        #sumar todos los salarios
        totalSalarios = totalSalarios + salarioActualEmpleado
        print(f"El total de los salarios hasta ahora es: {totalSalarios}")
        #restar el total de las edades con el total de los salarios
        print(f"El usuario es {nombreEmpleado}, su edad es {edadEmpleado}, y su salario es {salarioActualEmpleado}")
        j = j +1
    operacionEdadesSalarios = totalSalarios - totalEdades
    print(f"El total de la operacion totalSalarios - totalEdades es: {operacionEdadesSalarios}")
    print(f"el promedio es {totalEdades/contador}")


else:
    print("opcion no reconocida")