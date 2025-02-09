import sys
import os
from flowlogparser import parse_iana_protocol_numbers, load_lookup_table, parse_flow_log, write_output

def main():
    if len(sys.argv) != 5:
        print("Usage: python main.py <flow_log_file> <lookup_file> <protocol_file> <output_file>")
        return

    flow_log_file = sys.argv[1]
    lookup_file = sys.argv[2]
    iana_protocol_file = sys.argv[3]
    output_file = sys.argv[4]

    print(f"Processing with files: {flow_log_file}, {lookup_file}, {iana_protocol_file}, {output_file}")

    if not all(os.path.exists(f) for f in [flow_log_file, lookup_file, iana_protocol_file]):
        print("Error: One or more input files are missing.")
        return
    
    iana_protocols = parse_iana_protocol_numbers(iana_protocol_file)
    lookup_dict = load_lookup_table(lookup_file)
    tag_count, port_protocol_count, untagged_count = parse_flow_log(flow_log_file, lookup_dict, iana_protocols)
    
    print(f"Writing output to: {output_file}")
    write_output(tag_count, port_protocol_count, untagged_count, output_file)
    print("Processing complete.")

if __name__ == "__main__":
    main()