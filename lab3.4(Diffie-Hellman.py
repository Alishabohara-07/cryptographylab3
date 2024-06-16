def prime_checker(p):
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1

def primitive_check(g, p, L):
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
    return 1

l = []
# Change the value of P (prime number)
P = 23  # For example

# Check if P is prime
if prime_checker(P) == -1:
    print("Number Is Not Prime, Please Enter Again!")
    exit()

while True:
    # Change the value of G (primitive root)
    G = 5  # For example
    if primitive_check(G, P, l) == -1:
        print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
        continue
    break

# Change the values of private keys for User 1 and User 2
x1 = 6  # For example
x2 = 15  # For example

if x1 >= P or x2 >= P:
    print(f"Private Key Of Both The Users Should Be Less Than {P}!")
    exit()

# Calculate public keys
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Calculate shared secret keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nSecret Key For User 1 Is {k1}\nSecret Key For User 2 Is {k2}\n")

if k1 == k2:
    print("Keys Have Been Exchanged Successfully")
else:
    print("Keys Have Not Been Exchanged Successfully")
