num1 = float(input("Enter First Number :"))
num2 = float(input("Enter Second Number :"))

print ("Select Operation")
print ("1. Add")
print ("2. Subtract")
print ("3. Multiply")
print ("4. Divide")

choice = int(input("Select From 1-4 :"))
if choice == 1:
    result = num1+num2
elif choice == 2:
    result = num1-num2
elif choice == 3:
    result = num1*num2
elif choice == 4:
    result = num1/num2
else:
    print("Invalid Choice")

print("Result :", result)