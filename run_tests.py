import os
import subprocess
import filecmp
import shutil

TEST_DIR = "test_inputs"

def run_test(test_case):
    test_path = os.path.join(TEST_DIR, test_case)
    flow_log_src = os.path.join(test_path, "flow_log_data.txt")
    lookup_table_src = os.path.join(test_path, "example_lookup_table.csv")
    protocol_file = "protocol_numbers.txt"  # Shared for all test cases
    expected_output = os.path.join(test_path, "expected_output.csv")
    actual_output = os.path.join(test_path, "actual_output.csv")

    missing_files = [f for f in [flow_log_src, lookup_table_src, expected_output] if not os.path.exists(f)]
    if not all(os.path.exists(f) for f in [flow_log_src, lookup_table_src, expected_output]):
        print(f"{test_case}: MISSING FILES")
        return


    shutil.copy(flow_log_src, "flow_log_data.txt")
    shutil.copy(lookup_table_src, "example_lookup_table.csv")
    
    subprocess.run(["python", "main.py", "flow_log_data.txt", "example_lookup_table.csv", protocol_file, actual_output],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(actual_output):
        print(f"{test_case}: FAIL (No Output)")
        print(f"Expected output file: {actual_output}")
        print(f"Files in test case directory: {os.listdir(os.path.dirname(actual_output))}")
        return


    if filecmp.cmp(expected_output, actual_output):
        print(f"{test_case}: PASS")
    else:
        print(f"{test_case}: FAIL")

TEST_CASES = ["test_case_1", "test_case_2", "test_case_3"]
for test_case in TEST_CASES:
    run_test(test_case)