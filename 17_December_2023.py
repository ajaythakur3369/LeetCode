'''
1. Directions: If a + b means a is the sister of b,
a – b means a is the brother of b,
a ψ b means a is the daughter of b,
a π b means a is the mother of b. Which of the following relationships shows that I and n are wife and husband? 
Answer:- I π m ψ n 
'''

'''
2. What will be the output of the following statement?
'''

print('e' in 'azmat')

'''
Output:- False
'''

'''
3. You are given a table Employee which has the following columns: id, FirstName, LastName.
You have to use a query to display all those employees whose first names start with the letter 'R' and end with the letter 'I'. Some queries are given below – 
(a)	SELECT * FROM Employee WHERE FirstName LIKE '%RI%';
(b)	SELECT * FROM Employee WHERE FirstName LIKE 'R%' AND FirstName LIKE '%I';
(c)	SELECT * FROM Employee WHERE FirstName LIKE 'R' AND 'I';
(d)	SELECT * FROM Employee WHERE FirstName LIKE 'R%I';
Choose the most appropriate option from below
Answer:- (b) and (d) 
'''

'''
4. What will be the output of this code?
'''

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def print_student_details(self):
        print(self.__name, end=" ")
        print(self.age)

s = Student("Rohan", 20)
s.print_student_details()

'''
Output:- Rohan 20
'''

'''
5. Which one of the following has the highest precedence in the expression?
Answer:- Parentheses
'''


















