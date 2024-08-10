# SMTP Checker v1.0

## Overview
This script is designed to check the validity of SMTP accounts. The SMTP accounts should be listed in a file, and each line in the file should follow a specific format. The script will attempt to connect to each SMTP server using the provided credentials and report whether the connection was successful.

### SMTP File Structure
Make sure your SMTP file follows this structure:
`domain|port|email|password`

Example:
`smtp.domain.com|465|example@domain.com|Password123`


## Usage
1. **Input File**: The script requires a file containing SMTP credentials. Each credential should be on a new line in the format specified above.
2. **Execution**: Run the script, and you will be prompted to enter the path to your SMTP file.
3. **Results**: The script will output the status of each SMTP account, indicating whether it is working or has failed.

### Execution
To run the script, simply execute it in your Python environment:
`python smtp_checker.py`

## Notes
-   Ensure that the SMTP file is correctly formatted and accessible.
-   The script includes error handling for connection issues, but make sure your credentials are accurate.
