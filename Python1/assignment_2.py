# open the file
file = open("GME_stock.csv")

# read file
text = file.read()

# split it based on new-line
lines = text.split("\n")

#print(lines[0])
#print(lines[-1])

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0


# we need to index 2, 3, 4, 5 from each line.
# we want to use for loop
for line in lines[1:]:
    #count_2 = 0
    cols = line.split(",")
    #print(cols[1])
    #print(cols[2])
    #print(cols[3])
    #print(cols[4])

    open_price = int(str(cols[1])[0:1])
    high_price = int(str(cols[2])[0:1])
    low_price = int(str(cols[3])[0:1])
    close_price = int(str(cols[4])[0:1])

    #first_digit = open_price[0:1]
    first_digit = int(str(cols[1])[0:1])

    if open_price == 1 or high_price == 1 or low_price == 1 or close_price == 1:
        count_1 +=1

    if open_price == 2 or high_price == 2 or low_price == 2 or close_price == 2:
        count_2 +=1

    if open_price == 3 or high_price == 3 or low_price == 3 or close_price == 3:
        count_3 +=1

    if open_price == 4 or high_price == 4 or low_price == 4 or close_price == 4:
        count_4 +=1

    if open_price == 5 or high_price == 5 or low_price == 5 or close_price == 5:
        count_5 +=1

    if open_price == 6 or high_price == 6 or low_price == 6 or close_price == 6:
        count_6 +=1

    if open_price == 7 or high_price == 7 or low_price == 7 or close_price == 7:
        count_7 +=1

    if open_price == 8 or high_price == 8 or low_price == 8 or close_price == 8:
        count_8 +=1

    if open_price == 9 or high_price == 9 or low_price == 9 or close_price == 9:
        count_9 +=1


print(count_1, "numbers that start with 1")
print(count_2, "numbers that start with 2")
print(count_3, "numbers that start with 3")
print(count_4, "numbers that start with 4")
print(count_5, "numbers that start with 5")
print(count_6, "numbers that start with 6")
print(count_7, "numbers that start with 7")
print(count_8, "numbers that start with 8")
print(count_9, "numbers that start with 9")
