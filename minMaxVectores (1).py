vector = []
maximo = posMax = int(0)
minimo = (0)
posMin = (0)

for i in range(5):
    vector.append(input("ingrese un numero: "))

for i in range(len(vector)):
    if(i == 0):
        maximo = vector[i]
        posMaximo = i
    else:
        if(vector[i] > maximo):
            maximo = vector[i]
            posMax = i
    
print(f"el maximo es {vector[posMax]} en la posicion {posMax} PERO el minimo es {vector[posMin]} en la posicion {posMin}")

for i in range(len(vector)):
    if(vector[i] < minimo):
        minimo = vector [i]
        posMin = i
print(f"El minimo {minimo} en la posicion {posMin}")

for i in range(len(vector)):
    print(f"Los datos del vector son {vector[i]}")