import re
sumval = 0
with open('C:\AoC23\Day1_trebuchet.txt') as file:
        for line in file:
                    match = re.search(r'[\d]',line)
                    x = match.group()
                    print(x)
                    match = re.search(r'[\d]',line[::-1])
                    y = match.group()
                    print(y)
                    print(line.rstrip())
                    print(line[::-1].lstrip())
                    z=x+y
                    print(z)
                    sumval = sumval + int(z)
print(sumval)