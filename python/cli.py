# cli.py

import sys

def cli():
    if len(sys.argv) == 1:
        print("\n\t\twhere")
        print("\t\tfind your files")
        print("\t\t@1.0.0")
        return
    try:
        name_of_file = sys.argv[1]
        return name_of_file
    except:
        instructions = """
            Usage:
            
                > where <file>

        """
        print(instructions)

        return 1

if cli() != None: print(cli())