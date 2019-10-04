numbers = [-2,0,-1]
max_so_far = 0
max_ending_here = 1

for i in numbers:

    if i == 0:
        max_ending_here = 1
        continue

    max_ending_here = max_ending_here * i

    if max_ending_here > max_so_far:
        max_so_far = max_ending_here

print(max_so_far)