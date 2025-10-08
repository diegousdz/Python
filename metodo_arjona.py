# New file
vector = [1, 2,3,4,5,6,7,8,9,10]
i = 0 
while i < len(vector):
    if vector[i] %2 == 0:
        vector.pop(i)
    else:
        i=i+1
        
    print(i, len(vector), vector, i<len(vector))