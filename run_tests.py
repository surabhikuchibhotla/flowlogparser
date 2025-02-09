import os
import subprocess
import filecmp
import shutil

TEST_DIR = "test_inputs"
BACKUP_DIR = "backup"

def backup_original_files():
    """ Back up the original files before running tests. """
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for file in ["flow_log_data.txt", "example_lookup_table.csv", "output.csv"]:
        if os.path.exists(file):
            shutil.copy(file, os.path.join(BACKUP_DIR, file))

def restore_original_files():
    """ Restore the original files after running tests. """
    for file in ["flow_log_data.txt", "example_lookup_table.csv", "output.csv"]:
        backup_file = os.path.join(BACKUP_DIR, file)
        if os.path.exists(backup_file):
            shutil.copy(backup_file, file)

def run_test(test_case):
    test_path = os.path.join(TEST_DIR, test_case)
    flow_log_src = os.path.join(test_path, "flow_log_data.txt")
    lookup_table_src = os.path.join(test_path, "example_lookup_table.csv")
    protocol_file = "protocol_numbers.txt"
    expected_output = os.path.join(test_path, "expected_output.csv")
    actual_output = os.path.join(test_path, "actual_output.csv")

    if not all(os.path.exists(f) for f in [flow_log_src, lookup_table_src, expected_output]):
        print(f"{test_case}: MISSING FILES")
        return

    subprocess.run(["python", "main.py", flow_log_src, lookup_table_src, protocol_file, actual_output],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if not os.path.exists(actual_output):
        print(f"{test_case}: FAIL (No Output)")
        return

    if filecmp.cmp(expected_output, actual_output):
        print(f"{test_case}: PASS")
    else:
        print(f"{test_case}: FAIL")

if __name__ == "__main__":
    backup_original_files()
    TEST_CASES = ["test_case_1", "test_case_2", "test_case_3"]
    for test_case in TEST_CASES:
        run_test(test_case)
    restore_original_files()
