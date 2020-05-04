"""
Remove duplicates and return length of the new string

"""

def removeDuplicates(nums):
    if len(nums)<2:
        return len(nums)
    # print(nums)
    i = 1
    while  i < len(nums):
        # print("len nums ",len(nums))
        # print("i",i,"\n")
        if nums[i] != nums[i-1]:
            i += 1
            # print("i+1",i,"\n")
        else:
            nums.pop(i)
            # print("pop",nums,"\n")
            
    return len(nums)

if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    
    print(removeDuplicates(nums))