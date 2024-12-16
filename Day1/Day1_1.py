import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

left_column = []
right_column = []

for line in data:
    split_line = line.split("   ")
    left_column.append(split_line[0])
    right_column.append(split_line[1])

left_column.sort()
right_column.sort()

total = 0
for i in range(len(data)):
    total += abs(int(left_column[i]) - int(right_column[i]))

print(total)