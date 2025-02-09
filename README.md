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
python main.py <flow_log_file> <lookup_file> <protocol_file> <output_file>
```

Example:
```sh
python main.py flow_log_data.txt example_lookup_table.csv protocol_numbers.txt output.csv
```

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

The output file `output.csv` contains Tag Counts and Port/Protocol Combination Counts. Refer to the output file `output.csv` for an example on how the output will look.

## Installation & Dependencies

- Uses only built-in Python libraries.
- Ensure all input files are formatted correctly to avoid errors.

## Running Test Cases

This project includes a set of predefined test cases in the `test_inputs/` directory. To run all test cases, use:

```sh
python run_tests.py
```

The script will automatically copy the relevant test files, execute `main.py`, and compare the output with expected results. It will print `PASS` or `FAIL` for each test case.

### Adding New Test Cases
To add a new test case:
1. Create a new folder under `test_inputs/`, e.g., `test_case_4`.
2. Add the required test files:
   - `flow_log_data.txt`
   - `example_lookup_table.csv`
   - `expected_output.csv`
3. Update `run_tests.py` by adding `"test_case_4"` to the `TEST_CASES` list.
4. Run the tests using `python run_tests.py`.
The output will be generated in `output.csv`.
