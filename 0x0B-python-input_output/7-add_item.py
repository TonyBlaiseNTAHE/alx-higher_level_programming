#!/usr/bin/python3
"""importing sys and json module
"""

import os
import sys

"""importing save_to_json and
   load_from_json_file
"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""defining add_item funtion that
   adds all arguments to a Python list,
   and then save them to a file
"""


def add_item(args, filename):
    if (os.path.exists(filename)):
        content = load_from_json_file(filename)
    else:
        content = []
    content.extend(args)
    save_to_json_file(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
