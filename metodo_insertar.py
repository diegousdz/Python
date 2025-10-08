vector = []
i = 0 

for i in range (3):
    vector.append(int(input("agrega un numero entero: ")))

while i < len(vector): 
    if vector[i] %2 != 0:
        vector.insert(i + 1,10)
        i = i + 1
    i+=1
    print(i, i<len(vector), vector, len(vector), i)
 