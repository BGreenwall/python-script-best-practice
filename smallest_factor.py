#!/usr/bin/env python3

# A script for getting the smallest prime factor of an integer.

import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    sys.exit(f"{sys.argv[0]}: Expecting one command line argument -- the integer for which to get the smallest factor")

# Validate if the provided argument is an integer
try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit(f"{sys.argv[0]}: Expecting a positive integer as input")

# Ensure the integer is positive
if n < 1:
    sys.exit(f"{sys.argv[0]}: Expecting a positive integer")

# Special case for 1
if n == 1:
    print("1 has no prime factors")
    sys.exit(0)

# Finding the smallest prime factor
smallest_prime_factor = None
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        smallest_prime_factor = i
        break

# Output the smallest prime factor or the number itself if it's prime
if smallest_prime_factor is None:
    print(n)
else:
    print(smallest_prime_factor)

