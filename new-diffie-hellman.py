import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_primitive_root(g, p):
    required_set = set(num for num in range(1, p))
    actual_set = set(pow(g, powers, p) for powers in range(1, p))
    return required_set == actual_set

def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===\n")

    try:
        p = int(input("Enter a large prime number (p): "))
        if not is_prime(p):
            print("Error: The number you entered is not prime.")
            return

        g = int(input("Enter a primitive root modulo p (g): "))
        if not is_primitive_root(g, p):
            print(f"Error: {g} is not a primitive root modulo {p}.")
            return

        choice = input("Do you want to generate random private keys? (y/n): ").lower()

        if choice == 'y':
            a = random.randint(2, p-2)
            b = random.randint(2, p-2)
            print(f"User A's private key (a): {a}")
            print(f"User B's private key (b): {b}")
        else:
            a = int(input("User A, enter your private key (a): "))
            b = int(input("User B, enter your private key (b): "))

        A = pow(g, a, p)  # A = g^a mod p
        B = pow(g, b, p)  # B = g^b mod p

        print(f"\nUser A sends public key: {A}")
        print(f"User B sends public key: {B}")

        shared_key_a = pow(B, a, p)  # (B^a) mod p
        shared_key_b = pow(A, b, p)  # (A^b) mod p

        print(f"\nUser A computes shared key: {shared_key_a}")
        print(f"User B computes shared key: {shared_key_b}")

        if shared_key_a == shared_key_b:
            print(f"\n✅ Shared secret established successfully! Key: {shared_key_a}")
        else:
            print("\n❌ Error: Keys do not match.")
    
    except ValueError:
        print("Error: Please enter valid integers only.")
        
diffie_hellman()