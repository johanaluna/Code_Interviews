from itertools import combinations

def pairAnagram(lista):
    counterPairs = 0
    x=[[i,tuple(sorted(list(str(i))))] for i in lista]
        # print(x)
    d= {}
    for i,j in x:
        if j not in d:
            d[j] = [i] 
        else:
            d[j].append(i) 
    # return(d.values())
    for x in d.values():
        if len(x)>1:
            for c in combinations(x,2):
                counterPairs += 1
    return counterPairs

if __name__ == "__main__":
    lista = [22,220, 53,248,53,824,482, 76,67, 113,311,131]
    print(pairAnagram(lista))
