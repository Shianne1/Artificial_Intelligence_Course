names = ["Peter", "Emree", "Richard", "Bao", "Destiny", "Gabe"]
print(names) # will print list
print(names[2]) # will print the element to that index
print(names[-1]) # will print the last element
print(names[-2]) # will print the second to last element

capitals = {"PA":"Harrisburg",
            "CA":"Sacramento",
            "GA":"Atlanta",
            1:40
            } # a dictionary list
print(capitals)

# print(capitals[1]) will not  work
# print(capitals[PA]) will not  work
print(capitals["PA"]) # will print the value pair

d_1 = {"a":1, "b":2, "c":3}
value = d_1.pop("b")
print(value) # output: 2
print(d_1) # putput: {'a':1, 'c':3}

value = d_1.pop("z", "Not found")
print(value)


# INDEX NOTATION
numbers = [10, 20, 30, 40, 50]

#Positive indexing starts from 0
print(numbers[0])
print(numbers[2])

#Negative indexing starts from -1
print(numbers[-1])
print(numbers[-3])

# SLICING
numbers = [10, 20, 30, 40, 50]
# : means everything in between
print(numbers[1:3]) # excluding the last index number
print(numbers[2:])
print(numbers[:3])
print(numbers[::2])


# Exercise
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# slice from start to end -1
print(numbers[1:5]) # 20, 30, 40, 50

# slice from start to the end of the sequence
print(numbers[4:]) # 50, 60, 70, 80, 90

# slice from the beginning to end-1
print(numbers[:5]) # 10, 20, 30 ,40 ,50

# slice from start to end-1 with a step size of step
print(numbers[1:5:2]) # 20, 40

# slice the entire sequence with a step size of step
print(numbers[::3]) # 10, 40, 70
