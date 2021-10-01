class Student():
    def __init__(self, first='', last='', ID=0):
        self.first_name_str = first
        self.last_name_str = last
        self.id_int = ID
    
    def __str__(self):
        return "{} {}, ID:{}".format\
            (self.first_name_str, self.last_name_str, self.id_int)

student1 = Student()
print(student1)
student2 = Student(first='jinho', last='seo', ID=125)
print(student2)


class Car():
    def __init__(self, model ="N/A", color="N/A", HP = 200, cylinder=4):
        self.model = model
        self.color = color
        self.HP = HP
        self.cylinder = cylinder

    def __str__(self):
        return '{},{},{}'

car1 = Car(model='Accord', color='Black')
print(car1)
print(car1.model, car1.color, car1.HP, car1.cylinder)

## adding new attributes
Car.class_attribute = 'hello'
car1.instance_attribute ="world"

print(Car.class_attribute)






#zebra is animal
#List = []
#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#        nums = input()
#        print(nums)
        # tempList = list()
        # for i in List:
        #     for j in range(i+1, len(List)):
        #         if( List[i] + List[j] == target):
        #             tempList.append(List[i])
        #             tempList.append(List[j])
        #             return tempList
        #         else:
        #             continue