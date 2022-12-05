
cals = []

maxi = 0
with open("input.txt", 'r') as fp:
    for line in fp:
        input = line.rstrip()
        if len(input) == 0:
            cals.append(maxi)
            maxi = 0
            continue
        maxi += int(input)
        

            
print(max(cals))