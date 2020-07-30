def nextGreatest(nums):
    """
    
    """
    
    i= len(nums)-1
    while i >0:
        if nums[i]> nums[i-1]:
            pivot = nums[i]
            nums[i] = nums[i-1]
            nums[i-1] = pivot
            return nums
        i-=1
    return nums[::-1]

if __name__ == "__main__":
    nums = [6,8,4,5,3,2]
    nums2 = [3,2,1]
    nums3 = [2,3,1]
    nums4 = [1,2,2,0]
    nums5 = [1,5,0]
    print(nextGreatest(nums))
    print(nextGreatest(nums2))
    print(nextGreatest(nums3))
    print(nextGreatest(nums4))
    print(nextGreatest(nums5))
    