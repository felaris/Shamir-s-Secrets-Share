import re

# Read the shares from the text file
shares = []
with open('./shares.txt', 'r') as file:
    for line in file:
        match = re.match(r'Share (\d+): (\d+)', line)
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            shares.append((x, y))

# Recover the secret using Lagrange interpolation
def interpolate(shares):
    total = 0
    for i, (x_i, y_i) in enumerate(shares):
        numerator = denominator = 1
        for j, (x_j, y_j) in enumerate(shares):
            if i != j:
                numerator *= -x_j
                denominator *= x_i - x_j
        total += y_i * numerator // denominator
    return total.to_bytes((total.bit_length() + 7) // 8, byteorder='big')


