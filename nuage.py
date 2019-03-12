#!/usr/bin/env python3
import sys
import yaml
import os

# Merge two dictionaries (conditional).
def merge(input_yaml, parent_yaml):
    # Loop over all dictionary variable.
    for key, val in parent_yaml.items():
        if (key in input_yaml):
            # Check for dictionary.
            if (isinstance(parent_yaml[key], dict) and isinstance(input_yaml[key], dict)):
                merge(input_yaml[key], parent_yaml[key])
            # Check for list
            elif (isinstance(parent_yaml[key], list) and isinstance(input_yaml[key], list)):
                for item in parent_yaml[key]:
                    input_yaml[key].append(item)
        # Add key if not exist already.
        else:
            input_yaml[key] = parent_yaml[key]

# Main business logic.
def main(path):
    # Split filename and current directory path.
    current_dir = os.path.split(path)[0]
    file_name = os.path.split(path)[1]

    # Read main input file.
    with open(path, 'r') as ymlfile:
        try:
            input_yaml = yaml.load(ymlfile)
            parent_file = os.path.split(current_dir)[0] + '/' + file_name
        except yaml.YAMLError as exc:
            print(exc)

    # Iterate over all directories while input file exists in each directory.
    while os.path.isfile(parent_file):
        parent_yaml = None
        # Read and merge each file.
        with open(parent_file, 'r') as ymlfile:
            try:
                parent_yaml = yaml.load(ymlfile)
                merge(input_yaml, parent_yaml)
            except yaml.YAMLError as exc:
                print(exc)
        # Change current directory.
        current_dir = os.path.split(parent_file)[0]

        # Check if we reached the top most parent directory.
        if current_dir == '.':
            parent_file = './' + file_name
        else:
            parent_file = os.path.split(current_dir)[0] + file_name

    # Return merged yaml output.
    return input_yaml

# Initialize
if __name__ == "__main__":
    # Check for appropriate arguments.
    if len(sys.argv) >= 2:
        path = sys.argv[1]
        path = path.rstrip('\/')
        # Check if input file path exists.
        if os.path.isfile(path):
            input_yaml = main(path)
            print(input_yaml)
        else:
            print('Invalid file path.')
    else:
        print('Missing argument.')

