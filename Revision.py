days=["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
for day in days:
   if day=="Sunday":
     print("its a holiday")
   else:
     print("you have to go to work")
element =days[2:4]
print(element)
a=days.pop(3)
print(a)