#Tupple means No change, Whereas List can be change
days = ("Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday")
print(days)
# del.days[0],append,remove,pop not possible in Tupple
print(days[1])
days=list(days) #type cast
days[0]="Sunday"
print(days)
days=tuple(days)#round bracket indicate Tuple,can get Tupple value, iterate
print(days)
for day in days:
    if day=="Sunday":
        print("today is OFf")
    else: 
        print("you have to go work today")
for day in range(0,len(days)):#range for values
    if days[day]=="Sunday":#based on index No           
        print("today is OFf")
    else: 
        print("you have to go work today")
