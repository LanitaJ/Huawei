# Task1. Sum of big numbers

# https://peps.python.org/pep-0237/

t = int(input())

for i in range(t):
    a, b = [int(x) for x in input().split()]
    print(f"Case {i + 1}:\n{a} + {b} = {a + b}\n")