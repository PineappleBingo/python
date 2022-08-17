def BinarySearch(nums, target):

    temp = nums[:]
    isFound = False

    while len(temp) >= 1:
        mid = int(len(temp) / 2)

        # case when target var is left-half of remaining list
        if target < temp[mid - 1]:
            temp = temp[:mid]
        # case when target var is right-half of remaining list
        elif target > temp[mid - 1]:
            temp = temp[mid:]
        # case when taret var is same as mid point
        else:
            isFound = True
            break

    if isFound:
        print("Target Found:", temp[mid - 1])
    else:
        print("Target Not Found")


nums = [1, 3, 5, 3, 8, 9, 10, 12]
print(nums)
BinarySearch(nums, 12)
