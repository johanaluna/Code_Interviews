"""
  8 || 4 || 2 || 1
"""
def DecBinary(n): 
    return((bin(n).replace("0b",""))[::-1])

def DecBinary2(n):
    return (format(n,"b")[::-1])

    
    
   

if __name__ == "__main__":
    
    print(DecBinary(8))
    print(DecBinary2(8))
