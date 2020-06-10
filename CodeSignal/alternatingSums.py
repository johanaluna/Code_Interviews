def alternatingSums(a):
    i = 0
    sln = [0]*2
    while i < len(a):
        if i%2==0:
            sln[0]+=a[i]
        else:
            sln[1]+=a[i]
        i += 1
        
    return sln
a = [50, 60, 60, 45, 70]

print(alternatingSums(a))