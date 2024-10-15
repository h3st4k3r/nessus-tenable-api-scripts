
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
- **Create a new scan**.
- **Launch a scan**.
- **Get the results of a scan**.
- **Delete a scan**.

### How to Use

1. **Download the script**:
   Clone this repository or download the `manage-scans.py` script to your machine.

2. **Configure the API keys**:
   Edit the `manage-scans.py` file and replace the `ACCESS_KEY` and `SECRET_KEY` values with your Nessus API keys.

3. **Configure your domain or IP**:
   Edit the `manage-scans.py` file and replace the `BASE_URL` value with your Nessus domain or IP.

4. **Run the script**:
   Use the following commands to interact with the Nessus API. Below are the available commands:

## Available Commands

### 1. List Active Scans

This command lists all current scans on the Nessus server.

```bash
python3 manage-scans.py list_scans
```

### 2. Create a New Scan

This command creates a new scan using a name and the specified targets (IPs or ranges). The script uses a default policy (modify the `policy_id` and `uuid` according to your configuration).

```bash
python3 manage-scans.py create_scan 'New Scan' '192.168.1.10,192.168.1.20'
```

**Parameters**:
- **name**: Name of the scan.
- **targets**: List of IPs or IP ranges separated by commas.

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

## Script Structure

The `manage-scans.py` script is divided into several functions, which are triggered based on the argument passed when the script is run.

### Key Functions:

- **`list_scans()`**: Retrieves the list of scans.
- **`create_scan(name, targets)`**: Creates a new scan using the specified name and targets.
- **`launch_scan(scan_id)`**: Launches the scan with the provided ID.
- **`get_scan_results(scan_id)`**: Retrieves the results of the scan.
- **`delete_scan(scan_id)`**: Deletes the scan with the provided ID.

Each function interacts with the Nessus API using HTTP requests and processes the results in JSON format. The script also uses the `sys` library to handle command-line arguments and facilitate the execution of different functions.
