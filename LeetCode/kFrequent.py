def topKFrequent(nums, k) :
    dic = {}
        
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    print("solo", sorted(dic.items() ) ) 
    print(sorted(dic.items())[-2:])

if __name__ == "__main__":
    nums = [-1,54,16,16,3,54,]
    k=2
    print(topKFrequent(nums, k))