vector = []
for i in range(10):
    vector.append(int(input("agregar numero: ")))

for i in range(len(vector) -1, -1, -1):
    if(vector[i]%2 != 0):
        vector.insert(i+1, 999)

    print(i, i<len(vector), vector, len(vector), i)