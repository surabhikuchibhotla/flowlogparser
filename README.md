# Flow Log Parser

## Overview

This program processes flow logs, maps each entry to a tag based on a lookup table, and generates output summarizing tag counts and port/protocol combinations.

## File Descriptions

- **`main.py`**: The entry point for running the program.
- **`flowlogparser.py`**: Contains functions for parsing protocol numbers, lookup tables, and flow logs.
- **`flow_log_data.txt`**: Sample flow log data to be processed.
- **`example_lookup_table.csv`**: CSV file mapping destination ports and protocols to tags.
- **`protocol_numbers.txt`**: IANA-provided list of protocol numbers.
- **`output.csv`**: The generated output summarizing tag counts and port/protocol combinations.

## Usage

Run the program using:

```sh
python main.py
```

The script uses predefined file paths. Ensure all input files are in the same directory. If you want to change the files that are being uploaded, add them to the directory and change the file path names in the main.py file.

## Assumptions

1. **Log Format**: Only supports AWS VPC flow logs (version 2).
2. **Case Sensitivity: Matches in the lookup table are case-insensitive.**
3. **Protocol Mapping**: Extracts protocol mappings from `protocol_numbers.txt`.
4. **Untagged Entries**: Entries without a lookup match are marked as "Untagged."
5. **Data Limits**:
   - The flow log file can be up to **10MB**.
   - The lookup file can have up to **10,000 mappings**.
6. **Skipping Malformed Entries**: Any log entry with fewer than 14 fields is ignored.
7. **Protocol Numbers**: Uses `protocol_numbers.txt` to resolve protocol names dynamically.

## Output Format

The output file `output.csv` contains ### Tag Counts and ### Port/Protocol Combination Counts.

## Installation & Dependencies

- Uses only built-in Python libraries.
- Ensure all input files are formatted correctly to avoid errors.

## Testing

- Run the script with sample log files.
- Verify output matches expected results.
