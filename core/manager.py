"""
This module contains the LicenseManager class responsible for managing 
the collection of software licenses.
"""

from core.models import License

class LicenseManager:
    """
    Manages a collection of License objects using lists and sets.
    """

    def __init__(self):
        """
        Initializes the manager with an empty list for licenses 
        and a set for unique providers.
        """
        # Use a List to store objects
        self.licenses = []
        # Use a Set for unique values (Providers)
        self.providers = set()

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
        self.providers.add(license_obj.provider)
        return True

    def get_all_licenses(self) -> list:
        """
        Returns the list of all registered licenses.
        """
        return self.licenses

    def get_unique_providers(self) -> set:
        """
        Returns a set of all unique software providers.
        """
        return self.providers

    def calculate_total_monthly_cost(self) -> float:
        """
        Calculates the sum of monthly costs for all licenses.
        Requirement: Use control structures and math operations.
        """
        total = 0.0
        for lic in self.licenses:
            total += lic.monthly_cost
        return round(total, 2)