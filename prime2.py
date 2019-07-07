num = int(input("Enter a no: " ))
if num==1 or num <=0:
    print(num, "is not prime no")
elif num==2:
    print(num, "is prime no")
else:
    iter =1
    for i in range(2, num):
        iter+= 1
        if num%i==0
         break
    if iter == num:
        print(num, 'is prime')
    else:
        print (num, 'is not prime')