# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("Area of rectangle:", self.length * self.width)

#     def perimeter(self):
#         print("Perimeter of rectangle:", 2 * (self.length + self.width))


# rect = Rectangle(10, 5)

# rect.area()
# rect.perimeter()


# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def average(self):
#         avg = (self.marks1 + self.marks2 + self.marks3) / 3
#         print("Student Name:", self.name)
#         print("Average Marks:", avg)

# student1 = Student("Ali", 80, 75, 90)
# student1.average()

# class Student:
#     def __init__(self, name, marks1, marks2, marks3):
#         self.name = name
#         self.marks1 = marks1
#         self.marks2 = marks2
#         self.marks3 = marks3

#     def check_result(self):
#         average = (self.marks1 + self.marks2 + self.marks3) / 3

#         print("Student Name:", self.name)

#         if average >= 40:
#             print("Result: Passed")
#         else:
#             print("Result: Failed")

# student1 = Student("Ali", 45, 50, 35)
# student1.check_result()

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

acc1 = Account("123456789", 5000)

print("Account Number:", acc1.account_number)
print("Balance:", acc1.balance)
