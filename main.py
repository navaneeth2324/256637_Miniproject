import math
import function as f

print("--------------------Simple Calculator------------------")


while True:
    print("0.Exit")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power(a^b)")
    print("6.Modulus(a%\\b)")
    print("7.Factorial")
    print("8.GCD")
    print("9.SquareRoot(a)^(1/2)")
    print("10.Trignometric Functions")

    choice = input("Enter choice: ")

    if choice in ('0','1', '2', '3', '4', '5','6','7','8','9','10'):
        
        
        if choice == '0':
            print("Thank You! Bye")
            exit()

        elif choice == '1':
            f.add()

        elif choice == '2':
           f.subtract()
           

        elif choice == '3':
            f.multiply()
            

        elif choice == '4':
            f.divide()
            
        
        elif choice == '5':
            f.power()
            

        elif choice == '6':
            f.modulus()
            
    
        elif choice == '7':
            f.fact()
            
        
        elif choice == '8':
            f.findgcd()
            
        
        elif choice == '9':
            f.findsqroot()
        
        elif choice == '10':
            f.trignometry()
            
        
    else:
        print("Invalid Input")
