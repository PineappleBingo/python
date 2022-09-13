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
        print("The Number of Duplicate Products:", DuplicateProducts)


Sol = Solution()
Sol.displayInput()
Sol.FindDuplicate1(name, price, weight)
