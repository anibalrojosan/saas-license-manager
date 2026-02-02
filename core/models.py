"""
This module defines the License class, representing a software subscription.
"""

class License:
    """
    Represents a SaaS license with its basic attributes.
    """

    def __init__(self, license_id: int, name: str, provider: str, monthly_cost: float):
        """
        Initializes a new License instance.
        
        Args:
            license_id (int): Unique identifier for the license.
            name (str): Name of the software.
            provider (str): Company providing the service.
            monthly_cost (float): Monthly price of the subscription.
        """
        self.license_id = license_id
        self.name = name
        self.provider = provider
        self.monthly_cost = monthly_cost

    def to_dict(self) -> dict:
        """
        Converts the license object into a dictionary. Useful for data manipulation
        and storage.
        
        Returns:
            dict: A dictionary representation of the license.
        """
        return {
            "id": self.license_id,
            "name": self.name,
            "provider": self.provider,
            "monthly_cost": self.monthly_cost
        }

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the license.
        """
        return f"[{self.license_id}] {self.name} ({self.provider}) - ${self.monthly_cost}/mo"