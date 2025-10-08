# New file
vector = [1, 2,3,4,5,6,7,8,9,10]
i = 0 
for i in range(len(vector)-1, -1, -1):
    if(vector[i]%2 == 0):
        vector.pop(i)
        
    print(i, len(vector), vector, i<len(vector))