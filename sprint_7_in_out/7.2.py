import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    all_records = []
    seen_names = set()
    for file_path in input_files:
        single_file_records = get_records_from_file(file_path)
        append_to_all_records(all_records, seen_names, single_file_records)
    save_output_to_file(output_file, all_records)


def append_to_all_records(all_records, seen_names, single_file_records):
    for record in single_file_records:
        if record.get("name") and record["name"] not in seen_names:
            all_records.append(record)
            seen_names.add(record["name"])


def save_output_to_file(output_file, all_records):
    with open(output_file, 'w') as f:
        json.dump(all_records, f, indent=4)


def get_records_from_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return list(json.load(f))
    except FileNotFoundError:
        logging.error(f"File {file_path} doesn't exist")
        return []


parse_user("user4.json", "./7_2/user1.json", "./7_2/user2.json")
