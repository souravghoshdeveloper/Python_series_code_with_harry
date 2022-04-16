numbers = ["3", "34", "64"]

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])
# output --> 65


# map------------------------------------------------------------------
numbers = list(map(int, numbers))
numbers[2] = numbers[2] + 1
num = [2,3,]