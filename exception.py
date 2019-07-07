a={"Name":"Anum"}
# print(100/0)
# print("hello i am after exception")# File Not Found Exception, # File Not Open Exception, Index Out Range, program terminate abnormally in case
# try:
#     print(100/0)
# except:
#     print("Inside Exception Handler")
# print("hello I am after exception")
try:
    with open("data.csv", "r"):
        pass
    print(a["Name"])
except KeyError:
    print("this does not exist in this ADT")
except FileNotFoundError as e:
    print(e)
    print("file does noes not exist")
except Exception:# Generic Exception should be at last otherwise it would run it only
    print("this is an unknown error")
finally:
    print("I am finally Block")
print("Ending")