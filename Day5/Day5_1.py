import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
with open(os.path.join(script_dir, "data.txt")) as file:
  data = file.read().split('\n\n')

ruleset = data[0].split('\n')
pagenumbers = data[1].split('\n')

def find_rules (line):
  relevant_rules = []
  for rule in ruleset:
    single_rules = rule.split('|')
    if single_rules[0] in line and single_rules[1] in line:
      relevant_rules.append(single_rules)
  if relevant_rules:
    return True, relevant_rules

totallines = 0
totalmidnumber = 0

for line in pagenumbers:
  list_of_numbers = line.split(',')
  relevant_rules = []
  marked_incorrect=False
  if find_rules(list_of_numbers):
    result, relevant_rules = find_rules(list_of_numbers)
    if result:
      for rule in relevant_rules:
        if not (list_of_numbers.index(rule[0]) < list_of_numbers.index(rule[1])):
          marked_incorrect = True
  if not marked_incorrect:
    totallines += 1
    totalmidnumber += int(list_of_numbers[len(list_of_numbers) // 2])
  

print(f"Total lines: {totallines}")
print(f"Total midnumber: {totalmidnumber}")