with open('Day1_2_left.txt', 'r') as f:
    left = f.read().splitlines()
  
with open('Day1_2_right.txt', 'r') as f:
    right = f.read().splitlines()

int_left = [int(i) for i in left]
int_right = [int(i) for i in right]

total = 0
for i in int_left:
    total += (i * int_right.count(i))
    
print(total)