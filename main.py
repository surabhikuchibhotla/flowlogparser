from flowlogparser import parse_iana_protocol_numbers, load_lookup_table, parse_flow_log, write_output

def main():
    """ Main function to execute the flow log parsing and tagging process. """
    iana_protocol_file = "protocol_numbers.txt"
    lookup_file = "example_lookup_table.csv"
    flow_log_file = "flow_log_data.txt"
    output_file = "output.csv"

    # Load protocol mappings and lookup table
    iana_protocols = parse_iana_protocol_numbers(iana_protocol_file)
    lookup_dict = load_lookup_table(lookup_file)

    # Parse flow logs and generate counts
    tag_count, port_protocol_count, untagged_count = parse_flow_log(flow_log_file, lookup_dict, iana_protocols)

    # Write results to output file
    write_output(tag_count, port_protocol_count, untagged_count, output_file)

if __name__ == "__main__":
    main()
