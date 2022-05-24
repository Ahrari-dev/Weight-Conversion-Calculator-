weight = int(input("What is your weight? "))
conversion = str(input("(K)kg or (L)lb? "))
if conversion == "K":
    conversion1 = weight * 0.45
    print("You're weight is " + str(conversion1) + " in pounds!")
elif conversion == "L":
    conversion2 = wight / 0.45
    print("You're weight is " + str(conversion2) + " in kilograms!")
else:
    print("Invalid Info")
print("Thank you, Goodbye!")
