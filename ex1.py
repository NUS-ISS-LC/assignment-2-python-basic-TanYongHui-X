def find(number, target):
    for i in range(len(number)):
        difference = target - number[i]
        for j in range(len(number)):
            if i != j and difference == number[j]: # i != j make sures return two different indices.
                return [i, j]
    return None

print(find([2,5,10,13],7))
print(find([3,2,4],6))
print(find([3,3],6))