# Remember this 
class Test:
    def __init__(self, attr1, attr2):
        self.attribute_name1 = attr1
        self.attribute_name2 = attr2

# create an object
test1 = Test(10, 20)
print(test1.attribute_name1)   # 10
print(test1.attribute_name2)   # 20

# create an object
test2 = Test(100, 200)
print(test2.attribute_name1)   # 100
print(test2.attribute_name2)   # 200