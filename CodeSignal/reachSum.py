def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        return True

    elif s > target:
        return False # if we reach the number why bother to continue

    i=0
    while i < len(numbers):
        n = numbers[i]
        remaining = numbers[i + 1:]
        if subset_sum(remaining, target, partial + [n])==True:
            return True

        i+=1  
  
    return False

if __name__ == "__main__":
    numbers = [30, 35, 32, 30]
    print(subset_sum(numbers, 62))