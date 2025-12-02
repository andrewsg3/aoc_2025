import math

file = open("input.txt")

position = 0

stops_at_0 = 0

for line in file:
    change = int(line[1:])

    if line[0] == "L":
        change = -1 * change
    
    position += change 

    
    
    if position == 0 or position % 100 == 0:

        stops_at_0+=1
    
    print(f"{position}, {change}, {stops_at_0}")

print(stops_at_0)