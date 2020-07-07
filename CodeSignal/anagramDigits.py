def pairAnagram(lista):
    x=[[i,tuple(sorted(list(str(i))))] for i in lista]
        # print(x)
    d= {}
    for i,j in x:
        if j not in d:
            d[j] = [i] 
        else:
            d[j].append(i) 
    return(d.values())


if __name__ == "__main__":
    lista = [22,220, 53,248,53,824,482]
    print(pairAnagram(lista))