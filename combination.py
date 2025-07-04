import itertools

digits = input("Enter 3 digits: ")
combinations = itertools.permutations(digits)

for combination in combinations:
    print(''.join(combination))
