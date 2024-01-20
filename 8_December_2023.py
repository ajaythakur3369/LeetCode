'''
1. What will be the output of the following code?
'''

class A:
    def test1(self):
        print("method named test1 of A called")

class B(A):
    def test1(self):
        print("method named test1 of B called")

class C(A):
    def test1(self):
        print("method named test1 of C called")

class D(B, C):
    def test2(self):
        print("method named test2 of D called")

object1 = D()
object1.test1()

'''
Output:- One Two
'''

'''
2. What will be the output of this code?
'''

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

s = Student("Rohan", 60)
s.__name

'''
Output:- Error 
'''

'''
3. What will be the output of the following code?
'''

s = "abcd"
print(s[-2])
''''
Output:- c
'''

'''
4. What does 3^4 evaluate to? 
Answer:- 7
'''

'''
5. With what values do trigonometric functions work with angles in C++? 
Answer:- Radians
'''



























