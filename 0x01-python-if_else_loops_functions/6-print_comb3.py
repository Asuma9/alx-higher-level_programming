#!/usr/bin/python3
x = 0
for i in range(10):
    j = 1 + x
    while j < 10:
        print("{}{}".format(i, j), end="")
        if i == 8 and j == 9:
            break
        j += 1
        print(",", end=" ")
    x += 1
print("")
