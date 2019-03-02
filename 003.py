# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
# ------------------------------------------------
# Answer:6857


def largest_prime(num):
    factor = []

    while num != 1:
        for x in range(2, int(num+1)):
            if num % x == 0:
                num = num / x
                factor.append(x)
                break
    return max(factor)


if __name__ == '__main__':
    print(largest_prime(600851475143))
