"""
This module contains the LicenseManager class responsible for managing 
the collection of software licenses.
"""

from core.models import License
from collections import Counter
import json

class LicenseManager:
    """
    Manages a collection of License objects using lists and sets.
    """

    def __init__(self):
        """
        Initializes the manager with an empty list for licenses 
        and a set for unique providers.
        """
        self.licenses = []
        self._provider_counts = Counter()

    # --- Create ---
    def add_license(self, license_obj: License) -> bool:
        """
        Adds a new license to the system.
        
        Args:
            license_obj (License): The license instance to add.
            
        Returns:
            bool: True if added successfully, False otherwise.
        """
        # Validations could be added here (e.g., check if ID already exists)
        self.licenses.append(license_obj)
        self._provider_counts[license_obj.provider] += 1
        return True

    # --- Read ---
    def get_all_licenses(self) -> list:
        """
        Returns the list of all registered licenses.
        """
        return self.licenses
    
    def find_license_by_id(self, license_id: int) -> License:
        """
        Returns the license object with the given ID, or None if not found.

        Args:
            license_id (int): The ID of the license to search for.

        Returns:
            License: The license object with the given ID, or None if not found.
        """
        for license in self.licenses:
            if license.license_id == license_id:
                return license
        return None

    @property
    def providers(self) -> set:
        """
        Returns a set of all unique software providers.
        This is a read-only property that derives data from _provider_counts.
        """
        return set(self._provider_counts.keys())

    # --- Update ---

    def update_license_cost(self, license_id: int, new_cost: float) -> bool:
        """
        Updates the cost of the license with the given ID.

        Args:
            license_id (int): The ID of the license to update.
            new_cost (float): The new cost of the license.

        Returns:
            bool: True if updated successfully, False otherwise.
        """
        lic = self.find_license_by_id(license_id)
        if lic:
            lic.monthly_cost = new_cost
            return True
        return False

    # --- Delete ---
    def remove_license(self, license_id: int) -> bool:
        """
        Deletes the license object with the given ID.

        Args:
            license_id (int): The ID of the license to remove.

        Returns:
            bool: True if removed successfully, False otherwise.
        """
        lic = self.find_license_by_id(license_id)
        if lic:
            self.licenses.remove(lic)
            self._provider_counts[lic.provider] -= 1
            # If count reaches 0, remove the provider from the counter
            if self._provider_counts[lic.provider] <= 0:
                del self._provider_counts[lic.provider]
            return True
        return False

    # --- Helper Methods ---

    def calculate_total_monthly_cost(self) -> float:
        """
        Calculates the sum of monthly costs for all licenses.
        """
        total = 0.0
        for lic in self.licenses:
            total += lic.monthly_cost
        return round(total, 2)

    def load_from_json(self, file_path: str) -> bool:
        """
        Loads license data from a JSON file and populates the manager.
        
        Args:
            file_path (str): The path to the JSON file.
            
        Returns:
            bool: True if loaded successfully, False otherwise.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                
                for item in data:
                    # Create a real License object for each entry
                    # This automatically updates the Counter and Licenses list
                    new_license = License(
                        license_id=item['id'],
                        name=item['name'],
                        provider=item['provider'],
                        monthly_cost=item['monthly_cost']
                    )
                    self.add_license(new_license)
                    
            print(f"Successfully loaded {len(data)} licenses from {file_path}")
            return True
            
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return False
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from {file_path}.")
            return False
        except KeyError as e:
            print(f"Error: Missing expected field in JSON: {e}")
            return False

    def save_to_json(self, file_path: str) -> bool:
        """
        Saves the current list of licenses to a JSON file.
        """
        try:
            # Convert all License objects to dictionaries
            data_to_save = [lic.to_dict() for lic in self.licenses]
            
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    # --- Reporting & Filtering ---

    def get_licenses_by_provider(self, provider_name: str) -> list:
        """
        Args:
            provider_name (str): The name of the provider to filter by.

        Returns:
            list: A list of licenses that belong to the specified provider.
        """
        return [lic for lic in self.licenses if lic.provider.lower() == provider_name.lower()]

    def get_expensive_licenses(self, threshold: float) -> list:
        """
        Args:
            threshold (float): The threshold cost to filter by.

        Returns:
            list: A list of licenses with a monthly cost higher than the threshold.
        """
        return [lic for lic in self.licenses if lic.monthly_cost > threshold]

    def get_summary_statistics(self) -> dict:
        """
        Args:
            None

        Returns:
            dict: A dictionary with key metrics of the system.
        """
        total_licenses = len(self.licenses)
        total_cost = self.calculate_total_monthly_cost()
        
        # Avoid division by zero
        average_cost = round(total_cost / total_licenses, 2) if total_licenses > 0 else 0.0
        
        return {
            "total_count": total_licenses,
            "unique_providers_count": len(self.providers),
            "total_monthly_spend": total_cost,
            "average_license_cost": average_cost
        }
