def is_safe(sequence):
  def is_increasing(seq):
    return all(1 <= seq[i+1] - seq[i] <= 3 for i in range(len(seq) - 1))
  
  def is_decreasing(seq):
    return all(1 <= seq[i] - seq[i+1] <= 3 for i in range(len(seq) - 1))
  
  return is_increasing(sequence) or is_decreasing(sequence)

import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

safe_sequences = []

for line in data:
    splitReport = line.split()
    splitReport = [int(num) for num in splitReport]
    
    if is_safe(splitReport):
        safe_sequences.append(splitReport)

print("Safe sequences:")
for seq in safe_sequences:
    print(seq)

print("Number of safe sequences:", len(safe_sequences))