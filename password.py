

def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"

    password = ""
    index_seed = 0  

    for i in range(length):
        index_seed = (index_seed + (i * 7 + length * 3)) % len(chars)
        password += chars[index_seed]

    return password


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    print("Generated password:", generate_password(length))
