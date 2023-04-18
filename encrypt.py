import secrets

# The secret to be shared
secret = b'My secret message'

# The number of shares to be generated
n = 5

# The threshold number of shares required to reconstruct the secret
k = 3

# Generate random coefficients for the polynomial
coefficients = [secrets.randbits(256) for i in range(k-1)]
coefficients = [int.from_bytes(secret, byteorder='big')] + coefficients

# Define the polynomial function
def polynomial(x):
    result = 0
    for i, c in enumerate(coefficients):
        result += c * (x ** i)
    return result

# Generate shares
shares = []
for i in range(1, n+1):
    x = i
    y = polynomial(x)
    shares.append((x, y))

''' # Write the shares to a text file
with open('shares.txt', 'w') as file:
    for share in shares:'''
        #file.write(f'Share {share[0]}: {share[1]}\n') 

# Print the shares
for share in shares:
    print(f'Share {share[0]}: {share[1]}')

''' 

from functools import reduce
from operator import mul

# The shares to be combined
shares_to_combine = [shares[0], shares[2], shares[4]]

# The reconstructed x value
x_values = [share[0] for share in shares_to_combine]

# Lagrange interpolation to find the y value at x=0
def interpolate(x, shares):
    result = 0
    for j, share_j in enumerate(shares):
        yj = share_j[1]
        numerator = denominator = 1
        for m, share_m in enumerate(shares):
            if j != m:
                xm = share_m[0]
                numerator *= (x - xm)
                denominator *= (xm - xj)
        result += yj * (numerator / denominator)
    return result

# Reconstruct the secret
reconstructed_secret = interpolate(0, shares_to_combine)

# Print the reconstructed secret
print(f'Reconstructed secret: {reconstructed_secret.to_bytes((reconstructed_secret.bit_length() + 7) // 8, byteorder="big")}')


 '''