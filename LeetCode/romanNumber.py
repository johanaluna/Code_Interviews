def romanToInt(s):
    mapping={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result=[]   #create a list for saving the numbers which were been translated
    for i in range(len(s)):
        result.insert(i,mapping[s[i]])  #translate the numbers from roman number
    for j in range(len(result)-1):  #compare each numbers in the result list
        if result[j]<result[j+1]:   #if number is smaller than the next number 
            result[j]=0-result[j]   #change this number to negtive  
    return sum(result)  #sum it up and finish!

if __name__ == "__main__":
    print(romanToInt("IX"))