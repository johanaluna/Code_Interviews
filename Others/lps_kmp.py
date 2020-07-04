def lps(substring,i=1, j=0):
    sln = [None]*len(substring)
    sln[0] = 0
    while i < len(substring):
        if substring[i] == substring[j]:
            sln[i] = j+1
            j += 1
        elif substring[i] != substring[j]:
            if j==0:
                sln[i] = 0
            else:
                j = sln[j-1]
                i -= 1
        i += 1
    return(sln)

def kmp(string, substring, lps):
    i = j = 0
    while i < len(string):

        if string[i] == substring [j]:
            i += 1
            j += 1
        else: 
            if j != 0:
                j = lps[j-1]
            else: 
                i += 1
        if j == len(substring):
            print(i-j)
            j = lps[j-1]

print(lps("aalunakkluna"))  