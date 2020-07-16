def intToRoman(n):
    roman = [("M", 1000),("D",500),("C",100),("L",50),("X",10),("V",5),("I",1)]
    i=0
    while i < len(roman):
        if i == 0:
            times = (n // roman[i][1])
            number = times * roman[i][0]
            n = n - (times *roman[i][1])

        elif i == len(roman)-1:
            times = (n % roman[i][1])
            number += times * roman[i][0]

        else:
            times = (n % roman[i-1][1]) // roman[i][1]
            number += times * roman[i][0]
            n = n - (times * roman[i][1])
        i += 1
    return(number)


if __name__ == "__main__":
    print(intToRoman(1580))