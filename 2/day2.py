data = open("input.csv", "r").read().split(",")

# Convert data to ranges of ints
for i in range(len(data)):
    data[i] = data[i].split("-")
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])

# Iterate through them
# O(n^2) ?
invalid = 0
for i in range(len(data)): # For each range we have been given
    try:
        invalid0 = invalid
        for n in range(data[i][0], data[i][1]+1): # And within each range
            n = str(n) 
            if len(str(n)) >= 2 and len(str(n)) % 2 == 0: # Catch single digits
                middle = int(len(n)/2)
                if n[0:middle] == n[middle:]:
                    # print(f"{n} is invalid")
                    invalid +=1
                    if len(n) % 2 != 0:
                        print(f"{n} is invalid")

        print(f"{data[i]}, invalid: {invalid-invalid0}")
    except Exception as e:
        print(f"Exception on {n}: {e}")


print(invalid)