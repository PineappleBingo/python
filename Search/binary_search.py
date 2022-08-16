def search(self, nums, target):
    while len(temp) > 1:
        mid = int(len(temp) / 2)
        print("mid:", mid)

        if target == temp[mid-1]:
            print("Target = Temp[mid]")
            print("Target:", temp[mid-1])
            break

        elif  target < temp[mid]:
            # 3 < 5
            temp = temp[:mid]
            print(temp)
            if target == temp[mid-1]:
                # return target
                print("target:", target)
                break
            else:
                print("position:" )
        else:
            temp = temp[mid:]
            print(temp)