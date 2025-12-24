import hashlib
import os

def calculate_hash(file_path):
    """
    Calculate SHA-256 hash of a file
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    file_path = input("Enter file path to monitor: ").strip()

    if not os.path.exists(file_path):
        print("Error: File does not exist.")
        return

    print("\nCalculating initial hash...")
    original_hash = calculate_hash(file_path)
    print("Original Hash:", original_hash)

    input("\nModify the file if you want, then press Enter to continue...")

    print("\nRecalculating hash...")
    new_hash = calculate_hash(file_path)
    print("New Hash:", new_hash)

    if original_hash == new_hash:
        print("\n[+] File integrity maintained. No changes detected.")
    else:
        print("\n[!] WARNING: File integrity compromised. File has been modified.")


if __name__ == "__main__":
    main()
