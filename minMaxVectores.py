maximo = posMax = minimo = posMin = 0
vector = []

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
        else:
            minimo = vector[i]
            posMin = i
    
print(f"el maximo es {vector[posMax]} en la posicion {posMax} PERO el minimo es {vector[posMin]} en la posicion {posMin}")

for i in range(len(vector)):
    print(f"Los datos del vector son {vector[i]}")