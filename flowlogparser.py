import csv
from collections import defaultdict

def parse_iana_protocol_numbers(file_path):
# loads protocol numbers and names from protocol_numbers.txt into a dictionary 
# protocol_numbers.txt got data from the Internet Assigned Numbers Authority (IANA) official website
    protocol_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.split()
            if len(parts) >= 2 and parts[0].isdigit():  # Ensure valid number entry
                protocol_number = parts[0].strip()
                protocol_name = parts[1].lower().strip()
                protocol_dict[protocol_number] = protocol_name  # Store in dict

    return protocol_dict


# translates lookup file (example_lookup_table.csv) into a dictionary for easier comparison
def load_lookup_table(lookup_file):
    lookup_dict = defaultdict(list)
    with open(lookup_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['dstport'].strip(), row['protocol'].lower().strip())
            lookup_dict[key].append(row['tag'])

    return lookup_dict

def parse_flow_log(flow_log_file, lookup_dict, iana_protocols):
    tag_count = defaultdict(int)
    port_protocol_count = defaultdict(int)
    untagged_count = 0

    with open(flow_log_file, mode='r', encoding="ascii") as file:
        for line in file:
            parts = line.split()
            if len(parts) < 14 or parts[0] != '2':
                continue

            dst_port = parts[5].strip()
            protocol_num = parts[7].strip()
            protocol_name = iana_protocols.get(protocol_num, 'unknown').lower().strip()

    
            key = (str(dst_port).strip(), str(protocol_name).strip())
            tags = lookup_dict.get(key, ["Untagged"])
            
            for tag in tags:
                tag_count[tag] += 1
            
            if "Untagged" in tags:
                untagged_count += 1
                tag_count["Untagged"] += 1

            port_protocol_count[key] += 1

        return tag_count, port_protocol_count, untagged_count



def write_output(tag_count, port_protocol_count, untagged_count, output_file):
    with open(output_file, mode='w', encoding="ascii") as file:
        # tag count 
        file.write("Tag Counts:\n")
        file.write("Tag, Count\n")

        for tag, count in tag_count.items():
            if tag!= "Untagged":
                file.write(f"{tag},{count}\n")
    
        file.write(f"Untagged, {untagged_count}\n\n")

        # port/protocol combinations + count
        file.write("Port/Porotocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")

        for (port, protocol), count in port_protocol_count.items():
            file.write(f"{port}, {protocol}, {count}\n")
