def groupAnagrams(strs):
    x=[[i,tuple(sorted(list(i)))] for i in strs]
        # print(x)
    d= {}
    for i,j in x:
        if j not in d:
            d[j] = [i] 
        else:
            d[j].append(i) 
    return(d.values())