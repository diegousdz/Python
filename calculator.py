#this is a calculator for the class of programming in the Up

print("Hello user this is a sequential calculator")

nombreUser = str(input("first enter your name "))
print(f"Great {nombreUser}, we are ready to start")
print("Please enter a number 1 if you want to sum")
print("Please enter a number 2 if you want to subtract")
print("Please enter a number 3 if you want to multiply")
print("Please enter a number 4 if you want to divide")
userPicker = int(input("Enter only whole numbers between 1 and 4: "))
if (userPicker == 1):
    userPickerValueSum1 = int(input("First Enter the first value you want to operate to Sum "))
    userPickerValueSum2 = int(input("First Enter the second value you want to operate to Sum "))
    calculationResultSum = userPickerValueSum1 + userPickerValueSum2
    print(f"{nombreUser} this is your calculation result for Sum {calculationResultSum}")

if (userPicker == 2):
    userPickerValueSubtract1 = int(input("First Enter the first value you want to operate to Subtract "))
    userPickerValueSubtract2 = int(input("First Enter the second value you want to operate to Subtract "))
    calculationResultSubtract = userPickerValueSubtract1 - userPickerValueSubtract2 

    print(f"{nombreUser} this is your calculation result for Subtract {calculationResultSubtract}")    

if (userPicker == 3):
    userPickerValueMultiply1 = int(input("First Enter the first value you want to operate to Multiply "))
    userPickerValueMultiply2 = int(input("First Enter the second value you want to operate to Multiply "))
    calculationResultMultiply = userPickerValueMultiply1 * userPickerValueMultiply2 

    print(f"{nombreUser} this is your calculation result for Multiply {calculationResultMultiply}")

if (userPicker == 4):   
    userPickerValueDivide1 = float(input("First Enter the first value you want to operate to Divide "))
    userPickerValueDivide2 = float(input("First Enter the second value you want to operate to Divide "))
    
    if (userPickerValueDivide2 == 0):
        print("no se puede realizar la division . Sin Definir")
    else: 
        calculationResultDivide = userPickerValueDivide1 / userPickerValueDivide2 
        print(f"{nombreUser} this is your calculation result for Divide {calculationResultDivide:2f}")