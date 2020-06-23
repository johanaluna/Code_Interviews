def concatenationsSum(a):
    
    suma = 0
    i = 0
    while i < len(a):
        j = 0
        while j < len(a):
            number = int(str(a[i]) + str(a[j]))
            suma += number
            j += 1
        i+=1
    return suma
a=[10,2,5]
print(concatenationsSum(a))