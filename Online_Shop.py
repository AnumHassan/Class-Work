'''
****************************ONLINE STORE MANAGEMENT SYSTEM*************************
**This Program Adds, Deletes and Seraches a student from in-memory list repository**
'''
Store={
0:{
    'shirt_color':'blue',
    'shirt_size':'medium',
    'shirt_price':30,
    'shirt_stock1':30,}
    'shirt_color':'green',
    'shirt_size':'small',
    'shirt_price':40,
    'shirt_stock2':10,
    'shirt3_color':'orange',
    'shirt3_size':'large',
    'shirt3_price':50,
    'shirt_stock3':5,
    },
    1:{
    'bottom1_color':'blue',
    'bottom1_size':'medium',
    'bottom1_price':30,
    'bottom_stock1':30,
    'bottom2_color':'green',
    'bottom2_size':'small',
    'bottom2_price':40,
    'bottom_stock2':2,
    'bottom3_color':'orange',
    'bottom3_size':'large',
    'bottom3_price':50,
    'bottom_stock3':1,
    },
}
while True:
    print('Press 1 to see the list of Shirt')
    print('Press 2 to see the list of bottom ')
    print('Press 3 to shop')
    print('Press 4 to Exit!')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        for y in Store[0]:
            print (y,':',Store[0][y])
    elif choice == 2:
        for y in Store[1]:
            print (y,':',Store[1][y])
    elif choice==3 :
        option = int(input('for shirt press 1, for bottom press 2: '))
        if option==1:
                color1=input( " Enter color of Shirt")
                size1=input( " Enter size of Shirt")
                if Store[0]['shirt_color'].lower()== color1.lower() & Store[0]['shirt_size'].lower()== size1.lower():
                    print(" item is added in bucket")
    elif choice == 4:
        break
    # elif choice == 2:
    #     name = input('Enter the name you want to search for! ')
    #     for student in students:
    #         if student['Name'].lower() == name.lower():
    #             print('Student with name ' + name + ' found and details are as follows!')
    #             print(student)
    # elif choice == 3:
    #     name = input('Enter the name you want to Delete for! ')
    #     for student in students:
    #         if student['Name'].lower() == name.lower():
    #             del student['Name']
    #             del student['Father Name']
    #             del student['Cell Number']
    #             print(students)