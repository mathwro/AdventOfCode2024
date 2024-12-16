import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

total = 0
for line in data:
  line_index = data.index(line)
  char_list = list(line)
  for i in range(len(char_list)):
    char = char_list[i]
    if char == 'X':
      # Check forward
      if i+3 < len(char_list):
        if char_list[i+1] == 'M':
          if char_list[i+2] == 'A':
            if char_list[i+3] == 'S':
              total += 1
      # Check backward
      if i-3 >= 0:
        if char_list[i-1] == 'M':
          if char_list[i-2] == 'A':
            if char_list[i-3] == 'S':
             total += 1
      # Check downward
      if line_index + 3 < len(data):
        if data[line_index+1][i] == 'M':
          if data[line_index+2][i] == 'A':
            if data[line_index+3][i] == 'S':
              total += 1
      # Check upward
      if line_index - 3 >= 0:
        if data[line_index-1][i] == 'M':
          if data[line_index-2][i] == 'A':
            if data[line_index-3][i] == 'S':
              total += 1
      # Check diagonal down-right
      if i+3 < len(char_list) and line_index + 3 < len(data):
        if data[line_index+1][i+1] == 'M':
          if data[line_index+2][i+2] == 'A':
            if data[line_index+3][i+3] == 'S':
              total += 1
      # Check diagonal down-left
      if i-3 >= 0 and line_index + 3 < len(data):
        if data[line_index+1][i-1] == 'M':
          if data[line_index+2][i-2] == 'A':
            if data[line_index+3][i-3] == 'S':
              total += 1
      # Check diagonal up-right
      if i+3 < len(char_list) and line_index - 3 >= 0:
        if data[line_index-1][i+1] == 'M':
          if data[line_index-2][i+2] == 'A':
            if data[line_index-3][i+3] == 'S':
              total += 1
      # Check diagonal up-left
      if i-3 >= 0 and line_index - 3 >= 0:
        if data[line_index-1][i-1] == 'M':
          if data[line_index-2][i-2] == 'A':
            if data[line_index-3][i-3] == 'S':
              total += 1

print(total)