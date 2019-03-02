# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
# -----------------------------------------------------------
# Answer: 906609

palindromic_list = []
for n1 in range(1, 1000):
    for n2 in range(1, 1000):
        num1 = str(n1 * n2)
        num2 = num1[::-1]
        if num1 == num2:
            palindromic_list.append(int(num1))

print(max(palindromic_list))
