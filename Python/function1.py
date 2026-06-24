# Declartion and definition
# Function without parameter 
def add():
    a=10
    b=15
    a=a+b
    print("Addition is ",a)
add()

# Function with parameter
def sum(n1,n2):
    n1=n1+n2
    print("Sumation is",n1)

sum(50,25)

# Function with parameter and return
def sub(n1,n2):
    return n1-n2

res=sub(50,20)
print("Subtraction is ",res)