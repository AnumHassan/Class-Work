# def calculate_taxes(percent):
#     def actual_tax(salary): #inner function (can be use within this funtion for calling again again ) 
#         return salary*percent
#     return actual_tax
# actual_tax_fn=calculate_taxes(.3)
# print(actual_tax_fn)
# print(actual_tax_fn(100000))
def calculator(num1, num2, op):
    def add(n1,n2):
        return n1+n2
    def subract(n1,n2):
        return n1-n2
    if op=="-":
        return subract (num1,num2)
    if op=="+":
        return add (num1,num2)

print(calculator(2,3,"+"))
print(calculator(2,3,"-"))