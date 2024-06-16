def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result

# Define the range of values for n
start = 1  # Starting value
end = 20   # Ending value (inclusive)

# Calculate and print Euler's totient function for the range of values
for n in range(start, end + 1):
    print("phi(", n, ") =", phi(n))
