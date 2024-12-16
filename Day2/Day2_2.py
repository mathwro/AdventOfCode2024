import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
data = open(script_dir + "/data.txt").read().splitlines()

def is_monotonic(seq):
    if len(seq) <= 1:
        return True
    diff = seq[1] - seq[0]
    for i in range(len(seq)-1):
        if (seq[i+1] - seq[i]) * diff <= 0:
            return False
    return True

def valid_differences(seq):
    for i in range(len(seq)-1):
        diff = abs(seq[i+1] - seq[i])
        if diff < 1 or diff > 3:
            return False
    return True

def is_safe(seq):
    if not seq:
        return False
    numbers = [int(x) for x in seq.split()]
    
    # Check if already safe
    if is_monotonic(numbers) and valid_differences(numbers):
        return True
    
    # Check if removing one number makes it safe
    for i in range(len(numbers)):
        test_seq = numbers[:i] + numbers[i+1:]
        if is_monotonic(test_seq) and valid_differences(test_seq):
            return True
    
    return False

# Process each report
safe_count = sum(1 for report in data if is_safe(report))
print(f"Number of safe reports: {safe_count}")


