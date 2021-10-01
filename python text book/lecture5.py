
def simple_adder_1():
    sum = 0
    dataIter = "yes"
    while (dataIter[0] == "y" ):
        num = int(input("Please Enter Number : "))
        sum = sum + num

        data = input("Do you have more number? (Yes or No)")
        print(data)
        if (data[0] == "n") :
            break

    print("Total Sum : " + str(sum))
    #print("Total Sum : ", sum)

    #https://www.askpython.com/python/string/python-concatenate-string-and-int


def addSum_While():
    sum = 0
    xStr = input("Enter Number to Calculate <Enter to quit> : ")

    while xStr !="":
        num = int(xStr)
        sum = sum + num
        xStr = input("Enter Number to Calculate <Enter to quit>: ")
    print("Sum : ", sum)


def forloop_1(n):
    sum = 0
    for i in range(0,n,2):
        sum = sum + i
        print("sum : ", sum)

#forloop_1(10)

