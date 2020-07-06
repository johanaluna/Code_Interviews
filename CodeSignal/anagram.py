TEN = 10 
def updateFreq(n, freq) : 
    while (n) :  
        digit = n % TEN  
        freq[digit] += 1
        n //= TEN   
def areAnagrams(a, b):  
    freqA = [ 0 ] * TEN  
    freqB = [ 0 ] * TEN 
    updateFreq(a, freqA)  
    updateFreq(b, freqB)  
    for i in range(TEN):  
        if (freqA[i] != freqB[i]):  
            return False 
    return True
  


def pairAnagram(lista):
    # Driver code  
    total = 0
    for l in range(len(lista)):
        reminder = lista[l+1:]
        for j in range(len(reminder)):
            if (areAnagrams(lista[l], reminder[j])):  
                print("find 1 pair:",lista[l], lista[j])
                total += 1  
    return total


if __name__ == "__main__":
    lista = [22,220, 53,248,53,824,482]
    print(pairAnagram(lista))
