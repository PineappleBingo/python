name = ["ball", "glove", "box", "glove", "glove"]
price = [ 1, 2, 3, 1, 1]
weight = [1, 1, 2, 1, 1]


def FindDuplicate(name, price, weight):
    Products = list(zip(name, price, weight))
    list_Products = list()

    # swap tuple to list
    for prod in Products:
        list_Products.append(list(prod))

    print(list_Products)

FindDuplicate(name, price, weight)
# [['ball', 1, 1], ['glove', 2, 1], ['box', 3, 2], ['glove', 1, 1], ['glove', 1, 1]]