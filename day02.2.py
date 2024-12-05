with open("day02.txt", "r") as file:
    lines = file.readlines()


def is_line_safe(line):
    prev = None
    direction = None
    safe = True
    for el in line:
        if prev is None:
            prev = int(el)
            continue

        if (
            int(el) > prev
            and int(el) <= prev + 3
            and (direction is True or direction is None)
        ):
            prev = int(el)
            direction = True
        elif (
            int(el) < prev
            and int(el) >= prev - 3
            and (direction is False or direction is None)
        ):
            prev = int(el)
            direction = False
        else:
            safe = False
            break
    if safe:

        return True
    return False


splitlines = [line.split() for line in lines]
count = 0
for line in splitlines:
    if is_line_safe(line):
        count += 1
    else:
        for i in range(len(line)):
            line_copy = line.copy()
            line_copy.pop(i)
            if is_line_safe(line_copy):
                count += 1
                break
print(count)
