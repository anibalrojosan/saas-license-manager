import sys

def main_menu():
    print("\n--- SaaS License Management System ---")
    print("1. Add New License")
    print("2. List All Licenses")
    print("3. Remove License")
    print("4. Calculate Total Costs")
    print("5. Exit")
    
    choice = input("Select an option: ")
    return choice

def start():
    while True:
        option = main_menu()
        
        if option == "1":
            print("Feature: Add License (Coming soon)")
        elif option == "2":
            print("Feature: List Licenses (Coming soon)")
        elif option == "3":
            print("Feature: Remove License (Coming soon)")
        elif option == "4":
            print("Feature: Calculate Total Costs (Coming soon)")
        elif option == "5":
            print("Exiting system. Goodbye!")
            sys.exit()
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    start()