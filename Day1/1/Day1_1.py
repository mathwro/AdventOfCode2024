#left = [3, 4, 2, 1, 3, 3]
with open('Day1_1_left.txt', 'r') as f:
    left = f.read().splitlines()
  
with open('Day1_1_right.txt', 'r') as f:
    right = f.read().splitlines()

length = len(left)

left.sort()
right.sort()

total = 0
for i in range(length):
    total += abs(int(left[i]) - int(right[i]))

print(total)