#this is a calculator for the class of programming in the Up

print("Hello user this is a sequential calculator")

userName = str(input("first enter your name "))

userPickerValueSum1 = int(input("First Enter the first value you want to operate to Sum "))
userPickerValueSum2 = int(input("First Enter the second value you want to operate to Sum "))
calculationResultSum = userPickerValueSum1 + userPickerValueSum2

print(f"{userName} this is your calculation result for Sum {calculationResultSum}")

userPickerValueSubtract1 = int(input("First Enter the first value you want to operate to Subtract "))
userPickerValueSubtract2 = int(input("First Enter the second value you want to operate to Subtract "))
calculationResultSubtract = userPickerValueSubtract1 - userPickerValueSubtract2 

print(f"{userName} this is your calculation result for Subtract {calculationResultSubtract}")

userPickerValueMultiply1 = int(input("First Enter the first value you want to operate to Multiply "))
userPickerValueMultiply2 = int(input("First Enter the second value you want to operate to Multiply "))
calculationResultMultiply = userPickerValueMultiply1 * userPickerValueMultiply2 

print(f"{userName} this is your calculation result for Multiply {calculationResultMultiply}")

userPickerValueDivide1 = float(input("First Enter the first value you want to operate to Divide "))
userPickerValueDivide2 = float(input("First Enter the second value you want to operate to Divide "))
calculationResultDivide = userPickerValueDivide1 / userPickerValueDivide2 

print(f"{userName} this is your calculation result for Divide {calculationResultDivide:2f}")