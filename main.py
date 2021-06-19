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
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    print("GCD({},{}) =".format(n1,n2),math.gcd(n1, n2))

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

print("--------------------Simple Calculator------------------")


while True:
    print("0. Exit")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power(a^b)")
    print("6. Modulus(a%\\b)")
    print("7. Factorial")
    print("8. GCD")
    print("9. SquareRoot(a)^(1/2)")
    print("10. Trignometric Functions")

    choice = input("Enter choice: ")

    if choice in ('0','1', '2', '3', '4', '5','6','7','8','9','10'):
        
        
        if choice == '0':
            print("Thank You! Bye")
            exit()

        elif choice == '1':
            add()

        elif choice == '2':
           subtract()
           

        elif choice == '3':
            multiply()
            

        elif choice == '4':
            divide()
            
        
        elif choice == '5':
            power()
            

        elif choice == '6':
            modulus()
            
    
        elif choice == '7':
            fact()
            
        
        elif choice == '8':
            findgcd()
            
        
        elif choice == '9':
            findsqroot()
        
        elif choice == '10':
            trignometry()
            
        
    else:
        print("Invalid Input")
