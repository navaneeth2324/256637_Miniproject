import math
def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "+", num2, "=",num1+num2)
    

# This function subtracts two numbers
def subtract():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "-", num2, "=", num1- num2)

# This function multiplies two numbers
def multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "*", num2, "=", num1*num2)

# This function divides two numbers
def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(num1, "/", num2, "=", num1 / num2)

# This function calculates poer of 2 numbers
def power():
    num1 = float(input("Enter a: "))
    num2 = float(input("Enter b: "))
    print(num1, "^", num2, "=",num1**num2)

def modulus():
    num1 = float(input("Enter a: "))
    num2 = float(input("Enter b: "))
    print(num1, "%", num2, "=",math.fmod(num1, num2))

def fact():
    num=float(input("Enter number to find its factorial:"))
    print(num, "!" "=",math.factorial(num))

def findgcd():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    print("GCD({},{}) =".format(num1,num2),math.gcd(num1, num2))

def findsqroot():
    num=int(input("Enter number to find its square root:"))
    print("Square root({})=".format(num),int(math.sqrt(num)))

def trignometry():
    while True:
        print("****************************")
        deg=float(input("Enter degree:"))
        print("Sine({})".format(deg),math.sin(math.radians(deg)))
        print("Cosine({})".format(deg),math.cos(math.radians(deg)))
        print("Tan({})".format(deg),math.tan(math.radians(deg)))