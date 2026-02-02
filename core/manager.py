"""
This module contains the LicenseManager class responsible for managing 
the collection of software licenses.
"""

from core.models import License
from collections import Counter

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
