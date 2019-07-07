# # structural were difficult in real world and entites has attributes and characteristic, 
# #class templates anstandarize and oraganize information 
# # function are reusable(attribute,common), Classes are behaviour 
# class Human():
#     def __init__(self, name ="john"):
#         self.name=name
#         print("i am constructor")
#     def set_favourite_dish(self, favourite_dish):
#         self.favourite_dish=favourite_dish
#         print("i am constructor")
# h1= Human()
# h2= Human("john")
# h3=Human()
# h4=Human()
# print(h1.name)
# print(h2.name)
# h2.set_favourite_dish("biryani")
# print(h1.favourite_dish)
class student():
    def __init__ (self,name,age,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender
        self.age=age
    
    def print_details(self):
        print("NAME: ", self.name,"Age",self.age,"Rollno", self.rollno,"gender",self.gender)
student1=student("Umair",21,57,"male")
student1.print_details()
student1.name="Ammar"
student1.print_details()