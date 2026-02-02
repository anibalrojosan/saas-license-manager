import json
import random

def generate_sample_data(file_path="data/licenses.json", count=1000):
    providers = ["Microsoft", "AWS", "Google Cloud", "Salesforce", "Adobe", "Slack", "Atlassian", "Datadog"]
    softwares = ["Enterprise Suite", "Cloud Hosting", "Analytics Pro", "CRM Basic", "Creative Pack", "Team Chat", "Project Manager", "Monitoring Tool"]
    
    data = []
    for i in range(1, count + 1):
        provider = random.choice(providers)
        software = random.choice(softwares)
        license_data = {
            "id": i,
            "name": f"{provider} {software}",
            "provider": provider,
            "monthly_cost": round(random.uniform(10.0, 500.0), 2)
        }
        data.append(license_data)
    
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    
    print(f"Generated {count} licenses in {file_path}")

if __name__ == "__main__":
    generate_sample_data()