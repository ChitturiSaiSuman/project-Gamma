from cryptography.fernet import Fernet

def generate_key(password):
    # Ensure the password is bytes
    password_bytes = password.encode()

    # Generate a key using the password
    key = Fernet.generate_key()

    # Encrypt the key using the password
    fernet = Fernet(key)
    encrypted_key = fernet.encrypt(password_bytes)

    return encrypted_key

if __name__ == "__main__":
    encryption_password = "your_encryption_password_here"
    encrypted_key = generate_key(encryption_password)

    print("Encrypted Key:", encrypted_key)
