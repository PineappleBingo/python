name = ["ball", "glove", "box", "glove", "glove"]
price = [ 1, 2, 3, 1, 1]
weight = [1, 1, 2, 1, 1]

#Find duplicate product which has name, price, weight are the same

class Solution(object):
    def displayInput(self):
        return print(name, price, weight, sep="\n")

    def FindDuplicate1(self, name, price, weight):
        '''
        Keep track of duplicate product index by name, price, wegiht
        Time Complexity : O(3N)
        Space Complexity: ??
        '''
        dupleNameIndex = list()
        duplePriceIndex = list()
        dupleWeightIndex = list()
        DuplicateProducts = 0

        # check if there are duplicate name of products
        for i in range(len(name)):
            if name.count(name[i]) > 1:
                print("duplicate name index:", i)
                dupleNameIndex.append(i)

        # check if there are duplicate price of product out of duplicate product names
        for j in range(len(dupleNameIndex)):
            if price.count(price[dupleNameIndex[j]]) > 1:
                duplePriceIndex.append(dupleNameIndex[j])
                print("duplicate price out of duplicate product name index:", dupleNameIndex[j])
        
        # check if there are duplicate weight of product out of name and price matached
        for k in range(len(duplePriceIndex)):
            if weight.count(weight[duplePriceIndex[k]]) > 1:
                dupleWeightIndex.append(duplePriceIndex[k])
                print("duplicate weight out of duplicate product name and price matched index:", duplePriceIndex[k])

        DuplicateProducts = len(dupleWeightIndex)
        print("\nThe Number of Duplicate Products:", DuplicateProducts)

    # def FindDuplicate2(self, name, price, weight):
        # '''
        # Time Complexity : ??
        # Space Complexity: ??
        # '''
        # Products = list(zip(name, price, weight))
        # list_Products = list()

        # # swap tuple to list
        # for prod in Products:
        #     list_Products.append(list(prod))

        # print(Products)
        # print(list_Products)


        # DuplicateProducts = 0
        # DuplicateName = ""
        # DuplicatePrice = 0
        # DuplicateWeight = 0

        # DuplicateName = Products[0][0]
        # # "ball"
        # DuplicatePrice = Products[0][1]
        # # 1
        # DuplicateWeight = Products[0][2]
        # # 1

        # for i in range(len(list_Products)):
        #     # print(Products[i])

        #     print(DuplicateName)
        #     print(DuplicatePrice)
        #     print(DuplicateWeight)

        #     print(list_Products[i][0])

        #     for j in range(len(list_Products)):
                

        #     # if DuplicateName == Products[i][0]:
                

        #     # for j in range(len(list_Products)):
        #     #     if  DuplicateName == Products[i][0]:
        #     #         print("duplicate?:", Products[i][0])
                

        #     # if list_Products[i].count(list_Products[i][0]) > 1:
        #     #     print("Duplicates Found:", list_Products[i][0] )


        #     # if Products[i] == Products[i][0]:
        #     #     print("duplicate?:", Products[i][0])
            

        #     # for j in range(len(Products[i])):
        #     #     # if DuplicateName == Products[i][j]:
        #     #     print("Products:", Products[i][j])

        #     # print("")
        
        # # Products = {  }
        # return None


Sol = Solution()
Sol.displayInput()
Sol.FindDuplicate1(name, price, weight)
print("--------------------------------")
# Sol.displayInput()
# Sol.FindDuplicate2(name, price, weight)