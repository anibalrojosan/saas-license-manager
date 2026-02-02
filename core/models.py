def create_license(license_id, name, provider, cost):
    """
    Creates a license dictionary structure.
    """
    return {
        "id": license_id,
        "name": name,
        "provider": provider,
        "monthly_cost": float(cost)
    }