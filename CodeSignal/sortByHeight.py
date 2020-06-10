def sortByHeight(a):
    people = []
    for i in a:
        if i != -1:
            people.append(i)
    people.sort()

    i = j = 0
    while i < len(a):
        if a[i] != -1:
            a[i] = people[j]
            j += 1
        i += 1
    
    return a    


a= [-1, 150, 190, 170, -1, -1, 160, 180]
print(sortByHeight(a))