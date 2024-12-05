import re

with open("day03.txt", "r") as file:
    text = file.read()

matches = re.findall(r"mul\((\d+),(\d+)\)", text)
print(matches)

sum = 0
for match in matches:
    sum += int(match[0]) * int(match[1])

print(sum)
