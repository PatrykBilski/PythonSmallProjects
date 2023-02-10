#Thi

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def absolute(a):
    return abs(a)

def modulus(a, b):
    return a % b

def exponential(a, b):
    return a ** b

print("Please choose the operation that you want to perofmr from the following list:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Absolute Value")
print("6. Module - operation which returns the remainder")
print("7. Exponential\n")

while True:
    choice = input("Enter your choice: ")

    if (choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7'):
        try:
            a = float(input("First number: "))
            b = float(input("Second number: "))
        except ValueError:
            print("Invalid input. Please provide proper one")
            continue

        if choice == '1':            
            print(a, " + ", b, " = ",  addition(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

        if choice == '2':            
            print(a, " + ", b, " = ",  addition(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

        if choice == '3':            
            print(a, " + ", b, " = ",  addition(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

        if choice == '4':            
            print(a, " + ", b, " = ",  addition(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

        if choice == '5':
            
            mod = input("Please provide which number you want to have and absolute value of: ")
            if mod == 'a':
                print(absolute(a))
            elif mod =='b':
                print(absolute(b))
            else:
                print("Invalid input.")
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

        if choice == '6':
            print(a, " % ", b, " = ",  modulus(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break
        
        if choice == '7':            
            print(a, " ^ ", b, " = ",  exponential(a, b)) 
            print("\n Do you want to continue?")
            decision = input("Y/N: ")
            if (decision == "N" or decision == "n"):
                break
            elif (decision == 'Y' or decision == 'y'):
                continue
            else:
                print("Invalid input. The program will end now.")
                break

    else:
        print("Invalid input, do you want to start again or end the product?")   
        decision = input("Y/N: ")
        if (decision == "N" or decision == "n"):
            break
        elif (decision == 'Y' or decision == 'y'):
            continue
        else:
            print("Invalid input. The program will end now.")
            break