# New file
vector = [2]

minimo = vector[0]
posMin = 0

for i in range(len(vector)):
    if(vector[i] < minimo):
        minimo = vector [i]
        posMin = i
print(f"El minimo {minimo} en la posicion {posMin}")