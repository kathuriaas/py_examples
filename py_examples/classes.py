print("Start example1")


class Class1:
    v1 = 10


class_object1 = Class1()
print(class_object1.v1)


print("Start example2")
# All classes have __init__ function. It is always executed when class is initiated.
# self is parameter, equivalent to object created out of class


class Class2:
    def __init__(self):
        print("class2")


class_object2 = Class2()


print("Start example3")
# self parameter is reference to class itself


class Class3:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class_object3 = Class3(4, 5)
print(class_object3.x, class_object3.y)


print("Start example4")
# self parameter is reference to class itself


class Class4:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def method4(self):
        print(self.x)


class_object4 = Class4(4, 5)
print(class_object4.x, class_object4.y)
class_object4.method4()



