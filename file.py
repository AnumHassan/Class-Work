# # file read, write,
# inputdetails =input ("Enter Your Name") 
# with open("firstfile","w") as f : # file need to be closed as already open file 
#     f.write(inputdetails)
# file read, write,
# inputdetails =input ("Enter Your Name") 
# with open("firstfile","r") as f : # file need to be closed as already open file 
#     print(f.read())
# inputdetails =input ("Enter Your Name") 
# with open("firstfile","w") as f : # file need to be closed as already open file 
#     f.write("\n this is second line")  
inputdetails =input ("Enter Your Name") 
with open("firstfile","a") as f : # file need to be closed as already open file 
    f.write("\n this is scond line")     