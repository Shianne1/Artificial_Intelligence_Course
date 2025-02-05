credit = int(input("Enter the credit amount: "))

while (credit < 0) or (credit > 150):
    credit = int(input("\nInvalid credit. Try Again. \nEnter the credit amount: "))

if credit <= 30:
    print("Freshman")
elif credit <= 59:
    print("Sophomore")
elif credit <= 89:
    print("Junior")
else:
    print("Senior")
