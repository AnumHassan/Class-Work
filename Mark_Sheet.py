# Mark_Sheet
English = int(input("Enter Marks of English:"  ))
Islamiat = int(input("Enter Marks of Islamiat: " ))
Physics = int(input("Enter Marks of Physics: " ))
Chemistry = int(input("Enter Marks of Chemistry: " ))
Mathematics = int(input( "Enter Marks of Mathematics:"))
Obtained_Marks = English + Islamiat + Physics + Chemistry + Mathematics
Percentage=(Obtained_Marks/500)*100
if Percentage > 90:
    print ( "Your Grade is A+")
elif Percentage >80 and Percentage <= 90 :
    print("Your Grade is A")
elif Percentage >70 and Percentage <= 80 :
     print( "Your Grade is A-")
elif Percentage >60 and Percentage <= 70:
     print( "Your Grade is B")
elif Percentage >50 and Percentage <= 60:
     print( "Your Grade is C")
else:
    print( "Failed")
