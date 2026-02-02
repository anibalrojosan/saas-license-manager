"""
Main entry point for the SaaS License Management System.
Handles the User Interface and application loop.
"""
from core.manager import LicenseManager
from core.models import License

class MenuHandler:
    """
    Handles the console-based user interface and input validation.
    """
    def __init__(self):
        self.manager = LicenseManager()
        self.data_file = "data/licenses.json"
        self.manager.load_from_json(self.data_file)

    def _save_changes(self):
        """Helper to save changes to disk."""
        if self.manager.save_to_json(self.data_file):
            print("Changes saved to disk.")

    def display_menu(self):
        """Prints the main menu options."""
        print("\n" + "="*40)
        print("   SAAS LICENSE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. ➕ Add New License")
        print("2. 📋 List All Licenses")
        print("3. 🔍 Search License by ID")
        print("4. 💰 Update License Cost")
        print("5. ❌ Remove License")
        print("6. 📊 View System Statistics")
        print("7. 🏢 View Unique Providers")
        print("0. 🚪 Exit")
        print("="*40)

    def run(self):
        """
        Main application loop. Handles the user's choice and calls the appropriate method.
        The loop continues until the user chooses to exit.
        """
        while True:
            self.display_menu()
            choice = input("Select an option: ").strip()

            if choice == "1":
                self._add_license_menu()
            elif choice == "2":
                self._list_licenses()
            elif choice == "3":
                self._search_license()
            elif choice == "4":
                self._update_cost_menu()
            elif choice == "5":
                self._remove_license_menu()
            elif choice == "6":
                self._show_statistics()
            elif choice == "7":
                self._show_providers()
            elif choice == "0":
                print("\nExiting system. Thank you for using the SaaS License Management System!")
                break
            else:
                print("\nInvalid option. Please try again.")

    # --- Helper Methods ---

    def _add_license_menu(self):
        print("\n--- Add New License ---")
        try:
            lic_id = int(input("Enter License ID (Integer): "))
            name = input("Enter Software Name: ").strip()
            provider = input("Enter Provider Name: ").strip()
            cost = float(input("Enter Monthly Cost: "))

            if not name or not provider:
                print("Error: Name and Provider cannot be empty.")
                return

            new_lic = License(lic_id, name, provider, cost)
            if self.manager.add_license(new_lic):
                print(f"\nLicense '{name}' added successfully!")
                self._save_changes()
        except ValueError:
            print("\nError: Invalid input. Please enter numbers for ID and Cost.")

    def _list_licenses(self):
        licenses = self.manager.get_all_licenses()
        if not licenses:
            print("\nNo licenses found in the system.")
            return
        
        print("\n--- Current Licenses ---")
        for lic in licenses:
            print(lic)

    def _search_license(self):
        try:
            lic_id = int(input("\nEnter License ID to search: "))
            lic = self.manager.find_license_by_id(lic_id)
            if lic:
                print(f"\nFound: {lic}")
            else:
                print(f"\nLicense with ID {lic_id} not found.")
        except ValueError:
            print("\nError: Please enter a valid numeric ID.")

    def _update_cost_menu(self):
        try:
            lic_id = int(input("\nEnter License ID to update: "))
            new_cost = float(input("Enter New Monthly Cost: "))
            if self.manager.update_license_cost(lic_id, new_cost):
                print(f"\nCost updated successfully for ID {lic_id}.")
                self._save_changes()
            else:
                print(f"\nLicense with ID {lic_id} not found.")
        except ValueError:
            print("\nError: Invalid input. Please use numbers.")

    def _remove_license_menu(self):
        try:
            lic_id = int(input("\nEnter License ID to remove: "))
            if self.manager.remove_license(lic_id):
                print(f"\nLicense {lic_id} removed successfully.")
                self._save_changes()
            else:
                print(f"\nLicense with ID {lic_id} not found.")
        except ValueError:
            print("\nError: Invalid numeric ID required.")

    def _show_statistics(self):
        stats = self.manager.get_summary_statistics()
        print("\n--- System Statistics ---")
        print(f"Total Licenses: {stats['total_count']}")
        print(f"Unique Providers: {stats['unique_providers_count']}")
        print(f"Total Monthly Spend: ${stats['total_monthly_spend']:,}")
        print(f"Average License Cost: ${stats['average_license_cost']}")

    def _show_providers(self):
        providers = self.manager.providers
        if not providers:
            print("\nNo providers registered.")
            return
        print("\n--- Registered Providers ---")
        for p in sorted(providers):
            print(f"- {p}")

if __name__ == "__main__":
    app = MenuHandler()
    app.run()