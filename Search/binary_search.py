def search(nums, target):
    
    temp = nums[::]
    isFound = False
    
    while len(temp) > 1:
        mid = int(len(temp) / 2)

        # case when target found (Target = temp[mid-1])
        if target == temp[mid-1]:
            isFound = True
            break
        # case when target var is left-half of remaining list
        elif target < temp[mid]:
            temp = temp[:mid]
        # case when target var is right-half of remaining list    
        else:
            temp = temp[mid:]

    if isFound:
        print("Target Found:", temp[mid-1])
    else:
        print("Target Not Found")


nums = [1, 3, 5, 3, 8, 9, 10, 12]
search(nums, 10)