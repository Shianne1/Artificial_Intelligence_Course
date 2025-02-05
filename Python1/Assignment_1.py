GPA = float(input("Enter GPA: "))

while (GPA < 0.0) or (GPA > 4.0):
    GPA = float(input("Invalid GPA. Try Again. Enter GPA: "))

if GPA >= 3.5:
    print("Excellent")
elif (GPA >= 3.0) and (GPA <= 3.49):
    print("Good")
elif (GPA >= 2.0) and (GPA <= 2.99):
    print("Average")
else:
    print("Below Average")
