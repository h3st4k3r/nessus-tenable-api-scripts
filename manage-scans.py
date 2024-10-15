import requests
import json
import sys

# API keys provided
ACCESS_KEY = '53*****fe'
SECRET_KEY = 'b0*****40'

# Base URL for the Nessus API
BASE_URL = "https://localhost:8834"

# Headers for authentication
HEADERS = {
    "X-ApiKeys": f"accessKey={ACCESS_KEY}; secretKey={SECRET_KEY}",
    "Content-Type": "application/json"
}

# Function to list scans
def list_scans():
    url = f"{BASE_URL}/scans"
    response = requests.get(url, headers=HEADERS, verify=False)
    if response.status_code == 200:
        scans = response.json()
        print(json.dumps(scans, indent=2))
    else:
        print(f"Error listing scans: {response.status_code}")

# Function to launch a scan
def launch_scan(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}/launch"
    response = requests.post(url, headers=HEADERS, verify=False)
    if response.status_code == 200:
        print(f"Scan {scan_id} successfully launched.")
    else:
        print(f"Error launching scan: {response.status_code}")

# Function to create a scan with policy configuration
def create_scan(name, targets, uuid, policy_id):
    url = f"{BASE_URL}/scans"
    data = {
        "uuid": uuid,
        "settings": {
            "name": name,
            "enabled": True,
            "text_targets": targets,
            "policy_id": policy_id
        }
    }
    response = requests.post(url, headers=HEADERS, data=json.dumps(data), verify=False)
    if response.status_code == 200:
        scan = response.json()
        print(f"Scan created with ID: {scan['scan']['id']}")
    else:
        print(f"Error creating scan: {response.status_code}")

# Function to view scan results
def get_scan_results(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}"
    response = requests.get(url, headers=HEADERS, verify=False)
    if response.status_code == 200:
        results = response.json()
        print(json.dumps(results, indent=2))
    else:
        print(f"Error retrieving scan results: {response.status_code}")

# Function to delete a scan
def delete_scan(scan_id):
    url = f"{BASE_URL}/scans/{scan_id}"
    response = requests.delete(url, headers=HEADERS, verify=False)
    if response.status_code == 200:
        print(f"Scan {scan_id} successfully deleted.")
    else:
        print(f"Error deleting scan: {response.status_code}")

# Function to list scan policies
def list_policies():
    policies = nessus_api_call("/policies")
    if policies:
        print(json.dumps(policies, indent=2))
    else:
        print("Error al listar las políticas.")

# Main function
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <option> [parameters]")
        sys.exit(1)

    option = sys.argv[1]

    if option == "list_scans":
        list_scans()
    elif option == "launch_scan":
        if len(sys.argv) < 3:
            print("Scan ID is missing.")
            sys.exit(1)
        scan_id = sys.argv[2]
        launch_scan(scan_id)
    elif option == "create_scan":
        if len(sys.argv) < 5:
            print("Missing name, targets, UUID, and policy ID.")
            sys.exit(1)
        name = sys.argv[2]
        targets = sys.argv[3]
        uuid = sys.argv[4]
        policy_id = sys.argv[5]
        create_scan(name, targets, uuid, policy_id)
    elif option == "get_scan_results":
        if len(sys.argv) < 3:
            print("Scan ID is missing.")
            sys.exit(1)
        scan_id = sys.argv[2]
        get_scan_results(scan_id)
    elif option == "delete_scan":
        if len(sys.argv) < 3:
            print("Scan ID is missing.")
            sys.exit(1)
        scan_id = sys.argv[2]
        delete_scan(scan_id)
    elif option == "list_policies":
        list_policies()
    else:
        print(f"Invalid option {option}.")

if __name__ == "__main__":
    main()
