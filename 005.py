# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# ------------------------------------------------------------------
# Answer: 232792560

num = 20
while True:
    if all([num % x == 0 for x in range(20, 0, -1)]):
        break
    else:
        num += 20
print(num)
