#!/usr/bin/env bash

import os
import glob
import re
from datetime import datetime
import json
import pytz

def parse_filename(filename):
    pattern = r"(\d{8}_\d{6})_(\w+)\.json"
    match = re.match(pattern, filename)
    
    if match:
        datetime_str = match.group(1)
        sha_hash = match.group(2)

        # Parse datetime string into datetime object
        datetime_obj = datetime.strptime(datetime_str, "%Y%m%d_%H%M%S")

        return datetime_obj, sha_hash
    else:
        return None

def create_summary(repo_path, file_path, raw_output_path):
    print(repo_path)
    
    # Get a list of all .json files in the folder
    json_files = glob.glob("*.json", root_dir=raw_output_path)

    file_dict = {}
    for file in json_files:
        filename = os.path.basename(file)
        result = parse_filename(filename)

        if result:
            datetime_obj, sha_hash = result

            # Convert datetime to CET/CEST (Europe/Berlin)
            timezone = pytz.timezone('Europe/Berlin')
            datetime_cet = datetime_obj.replace(tzinfo=pytz.UTC).astimezone(timezone)

            # Print datetime as a single string in ISO 8601 format
            datetime_iso = datetime_cet.isoformat()

            file_dict[datetime_iso] = filename

        else:
            print("Filename", filename, "does not match the expected pattern.")

    # Output the file_dict to a JSON file
    json_output = os.path.join(raw_output_path, "summary", "file_dict.json")
    os.makedirs(os.path.dirname(json_output), exist_ok=True)
    with open(json_output, 'w') as file:
        json.dump(file_dict, file, sort_keys=True)

    print("JSON file generated:", json_output)

if __name__ == "__main__":
    if os.getenv("CI") == 'true':
        create_summary('demodiff_berlin', 'data/results.json', 'data_raw/berlin')
    else:
        from settings import repo_path, file_path, perform_output_dir_cleanup, raw_output_path
        create_summary(repo_path, file_path, raw_output_path)