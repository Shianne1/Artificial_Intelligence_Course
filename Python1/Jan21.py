number = int(input ("Enter an integer: "))
number = int(str(number)) # when trying to cast within another data type, you need to the data type it is orginally in then call the data type you want outside of that


last_character = int(str(number)[-1])  # will capture the last digit within a number
if last_character in (0,2,4,6,8):
    print(number,"is a even number")
if last_character in (1,3,5,7,9):
    print(number,"is a odd number")




if number % 2 == 0:
    print(number, " is even")
elif number % 2 != 0:
    print(number, " is odd")
else:
    print(number, " is neither even nor odd")