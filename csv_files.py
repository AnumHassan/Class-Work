#value comma seperated
#Module are file which we use it 
import csv
# with open("data.csv","r") as fdr:
#   students=csv.reader(fdr)
#   for student in students:
#       print(student)
Single_Student=["inam","Ai,3:30"]
Students=[
    ["inam","Ai,3:30"],
    ["Anum","Ai,3:30"],
    ["Umair","Ai,3:30"],
]
with open ("data.csv","w",newline="") as fdes:
    writer=csv.writer(fdes,delimiter=",")
    # writer.writerow(Single_Student)
    for Student in Students:
         writer.writerow(Student)
                
