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

int_left = [int(i) for i in left_column]
int_right = [int(i) for i in right_column]

total = 0
for i in int_left:
    total += (i * int_right.count(i))
    
print(total)