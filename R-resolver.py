#!/usr/bin/env python3
import os
import shutil
import fileinput
import argparse

PARENT_DIR="./Test"

def replacer(text_to_search, replacement_text):
    for root, dirs, files in os.walk(PARENT_DIR):
        print('--'*10)
        print(root)
        print(dirs)
        print(files)
        for file in files:
            if file.endswith('.java'):

                with open(os.path.join(root,file), 'r') as file1 :
                    filedata = file1.read()

                filedata = filedata.replace(text_to_search, replacement_text)

                with open(os.path.join(root,file), 'w') as file2:
                    file2.write(filedata)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    
    parser.add_argument('-o', '--old_file', type=str, required=True,  help="Old package name")
    parser.add_argument('-n', '--new_file', type=str, required=True,  help="New package name")
    args = parser.parse_args()
    

    replacer(args.old_file, args.new_file)