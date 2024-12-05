with open("day02.txt", "r") as file:
    lines = file.readlines()


splitlines = [line.split() for line in lines]
count = 0
for line in splitlines:
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
        print(line)
        count += 1
print(count)
