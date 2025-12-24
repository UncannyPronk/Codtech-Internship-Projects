from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    """
    Generate and save a secret key
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    """
    Load the previously generated key
    """
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)

    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "wb") as file:
        file.write(encrypted_data)

    print(f"[+] File encrypted successfully: {encrypted_file}")


def decrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    # Ask user how to save decrypted file
    print("\nChoose decryption output option:")
    print("1. Overwrite original file name")
    print("2. Create a new decrypted file (.dec)")

    option = input("Enter choice (1/2): ").strip()

    if option == "1":
        if file_path.endswith(".enc"):
            output_file = file_path.replace(".enc", "")
        else:
            output_file = file_path + ".dec"
    else:
        output_file = file_path.replace(".enc", ".dec")

    with open(output_file, "wb") as file:
        file.write(decrypted_data)

    print(f"[+] File decrypted successfully: {output_file}")


def main():
    print("=== Advanced Encryption Tool (AES-256) ===")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Select an option: ").strip()
    file_path = input("Enter file path: ").strip()

    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    if choice == "1":
        encrypt_file(file_path)
    elif choice == "2":
        decrypt_file(file_path)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
