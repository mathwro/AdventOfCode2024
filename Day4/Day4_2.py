import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

def out_of_bounds (line_index, char_list, i):
  return i+2 >= len(char_list) or line_index+2 >= len(data)

def mm (line_index, char_list):
  if char_list[i+2] == 'M' and list(data[line_index+2])[i] == 'S' and list(data[line_index+2])[i+2] == 'S' and list(data[line_index+1])[i+1] == 'A':
    return True
  
def ms (line_index, char_list):
  if char_list[i+2] == 'S' and list(data[line_index+2])[i] == 'M' and list(data[line_index+2])[i+2] == 'S' and list(data[line_index+1])[i+1] == 'A':
    return True

def ss (line_index, char_list):
  if char_list[i+2] == 'S' and list(data[line_index+2])[i] == 'M' and list(data[line_index+2])[i+2] == 'M' and list(data[line_index+1])[i+1] == 'A':
    return True
  
def sm (line_index, char_list):
  if char_list[i+2] == 'M' and list(data[line_index+2])[i] == 'S' and list(data[line_index+2])[i+2] == 'M' and list(data[line_index+1])[i+1] == 'A':
    return True

total = 0
for line in data:
  line_index = data.index(line)
  char_list = list(line)
  for i in range(len(char_list)):
    char = char_list[i]
    if char == 'M':
      if not out_of_bounds(line_index, char_list, i):
        if mm(line_index, char_list):
          total += 1
        if ms(line_index, char_list):
          total += 1

    if char == 'S':
      if not out_of_bounds(line_index, char_list, i):
        if ss(line_index, char_list):
          total += 1
        if sm(line_index, char_list):
          total += 1

print(total)