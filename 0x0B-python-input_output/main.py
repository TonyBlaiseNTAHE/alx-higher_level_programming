#!/usr/bin/python3

import json
import sys

def save_to_json_file(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_from_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def main():
    # Check if the JSON file exists and load data
    json_filename = "add_item.json"
    data = load_from_json_file(json_filename)

    # Parse command-line arguments and ignore the script name (sys.argv[0])
    arguments = sys.argv[1:]

    # Append new arguments to the existing data
    data.extend(arguments)

    # Save the updated data to the JSON file
    save_to_json_file(data, json_filename)

if __name__ == "__main__":
    main()
