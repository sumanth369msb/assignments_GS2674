####1.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    num1 = int(input("Enter the 1st number: "))
    num2 = int(input("Enter the 2nd number: "))

    res = num1 + num2

    print(res)

except ValueError as e:
    print("Not a valid number.")


######2. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    n = float(input("Enter a number)
    print(n)

except KeyboardInterrupt:
    print("\nInput canceled by the user.")


# 3. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    filePath = input("Enter the file path: ")
    with open(filePath, 'r') as file:
        file1 = file.read()
        print(file1)
except FileNotFoundError:
    print("The file not found.")
except UnicodeDecodeError as e:
    print(f"Unicode decode error - {e}")

            
#####4.Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    l1 = [11, 22, 33, 44, 55]
    length = a.length

except AttributeError as e:
    print("AttributeError:", e)
    
l1.insert(3,66)
print(l1)
