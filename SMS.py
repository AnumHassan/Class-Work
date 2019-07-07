Students=[]
Student={}
# for i in range(3):
#     Student = {}
#     Student["Name"]=input("Please Enter your Name ")
#     Student["Father Name"]=input("Please Enter your Father Name ")
#     Student["Cell No"]=input("Please Enter your Cell No ")
#     Students.append(Student)
# print("Currently enrolled Students", len(Students))
# for Student in Students:
#     print(Student)
while True:
    print("Press 1 to choose Add")
    print("Press 2 to choose Find")
    print("Press 3 to choose Delete")
    print("Press 4 to choose Exit")
    choice=int(input("Enter your Option"))
    if choice==1:
        n=int(input("How Many Student You want to add"))
        for i in range(n):
            Student["Name"]=input("Please Enter your Name ")
            Student["Father Name"]=input("Please Enter your Father Name ")
            Student["Cell No"]=input("Please Enter your Cell No ")
            Students.append(Student)
            print("Currently enrolled Students", len(Students))
    elif choice==2:
        name1=input("Enter Name you want to Search")
        for Student in Students:
            if Student["Name"].lower()==name1.lower:
                print("Student with name"+ name1 + "Found Detail are as Follow")
                print(Student)
            else:
                print("Not Found")
    elif choice==3:
        name2=input("Enter Name you want to Delete")
        for Student in Students:
            if Student["Name"].lower()==name2.lower:
                Student.pop["Name"]
                Student.pop["Father"]
                Student.pop["Father"]
                print(Students)
            else:
                print("Not Found")
    elif choice==3:
        print("Thank You")
    