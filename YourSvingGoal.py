print("Welcome to Savings Builder")
print("40% of your income will be saved")

income = float(input("Enter your income : "))

savings = income * .4
oneYear = savings * 12
fiveYear = oneYear * 5
Goal = 1000000 - fiveYear
print("----------------------------------------------------------------------")
print("Your savings will be: ", savings,"Rupees")
print("In one year you will save: ", oneYear,"Rupees")
print("In Five year you will be having a saving of : ", fiveYear ,"Rupees")
print("This money is need to reach your 10 lac goal : ", Goal,"Rupees")