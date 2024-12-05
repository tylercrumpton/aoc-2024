with open("day01.txt", "r") as file:
    lines = file.readlines()


list1 = []
list2 = []
for line in lines:
    item1, item2 = line.strip().split("   ")
    list1.append(int(item1))
    list2.append(int(item2))

list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])

print(total)
