import os


def is_safe(sequence):
    def is_increasing(seq):
        skips = 0
        i = 0
        while i < len(seq) - 1:
            if not (1 <= seq[i+1] - seq[i] <= 3):
                skips += 1
                if skips > 1:
                    return False
                if i < len(seq) - 2 and (1 <= seq[i+2] - seq[i] <= 3):
                    i += 1  # Skip the next element
                elif i == len(seq) - 2:
                    return True  # Allow the last element to be the odd one out
                else:
                    return False
            i += 1
        return True

    def is_decreasing(seq):
        skips = 0
        i = 0
        while i < len(seq) - 1:
            if not (1 <= seq[i] - seq[i+1] <= 3):
                skips += 1
                if skips > 1:
                    return False
                if i < len(seq) - 2 and (1 <= seq[i] - seq[i+2] <= 3):
                    i += 1  # Skip the next element
                elif i == len(seq) - 2:
                    return True  # Allow the last element to be the odd one out
                else:
                    return False
            i += 1
        return True

    if is_increasing(sequence) or is_decreasing(sequence):
        return True

    # Check if removing one element makes the sequence safe
    for i in range(len(sequence)):
        new_seq = sequence[:i] + sequence[i+1:]
        if is_increasing(new_seq) or is_decreasing(new_seq):
            return True

    return False

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

with open(os.path.join(script_dir, "Day2_2.txt"), 'r') as f:
    reports = f.read().splitlines()

safe_sequences = []

for line in reports:
    splitReport = line.split()
    splitReport = [int(num) for num in splitReport]
    
    if is_safe(splitReport):
        safe_sequences.append(splitReport)

print("Safe sequences:")
for seq in safe_sequences:
    print(seq)

print("Number of safe sequences:", len(safe_sequences))