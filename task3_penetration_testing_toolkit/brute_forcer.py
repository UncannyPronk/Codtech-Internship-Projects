def run():
    print("\n[INFO] This is a brute-force SIMULATION module")
    print("[INFO] No real authentication is performed\n")
    print("[INFO] Hardcoded username: admin\n")
    print("[INFO] All other usernames will fail.\n")

    username = input("Enter username: ").strip()

    # Simulated credentials (demo only)
    demo_user = "admin"
    demo_password = "admin"

    passwords = ["password", "123456", "admin", "root"]

    print("\nStarting brute-force simulation...\n")

    for pwd in passwords:
        print(f"Trying password: {pwd}")

        if username == demo_user and pwd == demo_password:
            print(f"\n[+] Password found for user '{username}': {pwd}")
            return

    print(f"\n[-] Password not found for user '{username}'.")
