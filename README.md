# Nessus API Automation with Python

This project enables interaction with the Nessus API using Python, automating tasks such as creating, launching, retrieving results, and deleting scans. It's useful for automating security workflows and managing scans via scripts without needing access to the Nessus web interface.

## Requirements

1. **Nessus installed** and running.
2. **Nessus API Keys**: You need the **Access Key** and **Secret Key**, which can be generated from the Nessus interface under the **API Keys** section.
3. **Python 3.x** installed.
4. Required Python libraries:
   - `requests`: To perform HTTP requests.
   - `json`: To handle the JSON data returned by the API.

### Installing Dependencies

Install the required `requests` library if it’s not already installed:

```bash
pip install requests
```

## Usage

This script supports the following functionalities:

- **List active scans**.
- **Create a new scan with a specific policy**.
- **Launch a scan**.
- **Get the results of a scan**.
- **Delete a scan**.
- **List available scan policies**.

### How to Use

1. **Download the script**:
   Clone this repository or download the `manage-scans.py` script to your machine.

2. **Configure the API keys**:
   Edit the `manage-scans.py` file and replace the `ACCESS_KEY` and `SECRET_KEY` values with your Nessus API keys.

3. **Run the script**:
   Use the following commands to interact with the Nessus API. Below are the available commands:

## Available Commands

### 1. List Active Scans

This command lists all current scans on the Nessus server.

```bash
python3 manage-scans.py list_scans
```

### 2. Create a New Scan with a Specific Policy

This command creates a new scan using a name, the specified targets (IPs or ranges), and a specific scan policy. You can list the available policies using the `list_policies` command.

```bash
python3 manage-scans.py create_scan "Scan Name" "192.168.1.10,192.168.1.20" "UUID_POLICY" POLICY_ID
```

**Parameters**:
- **name**: Name of the scan.
- **targets**: List of IPs or IP ranges separated by commas.
- **uuid**: The UUID of the policy you want to use (retrieved using `list_policies`).
- **policy_id**: The ID of the policy you want to use (retrieved using `list_policies`).

### 3. Launch a Scan

This command launches a predefined scan using its **ID**. You can obtain the scan IDs using the `list_scans` command.

```bash
python3 manage-scans.py launch_scan <scan_id>
```

**Parameters**:
- **scan_id**: The ID of the scan to launch.

### 4. Get Results of a Scan

This command retrieves the results of a completed scan using its **ID**.

```bash
python3 manage-scans.py get_scan_results <scan_id>
```

**Parameters**:
- **scan_id**: The ID of the scan to retrieve results from.

### 5. Delete a Scan

This command deletes an existing scan using its **ID**.

```bash
python3 manage-scans.py delete_scan <scan_id>
```

**Parameters**:
- **scan_id**: The ID of the scan you want to delete.

### 6. List Available Scan Policies

This command lists all available scan policies on the Nessus server, showing the policy name, UUID, and policy ID.

```bash
python3 manage-scans.py list_policies
```

This will display all available policies, allowing you to choose the appropriate `uuid` and `policy_id` when creating a new scan.
