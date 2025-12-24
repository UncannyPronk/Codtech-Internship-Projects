import port_scanner
import brute_forcer

def main():
    while True:
        print("\n=== Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Force Simulator")
        print("3. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            port_scanner.run()
        elif choice == "2":
            brute_forcer.run()
        elif choice == "3":
            print("Exiting toolkit.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
