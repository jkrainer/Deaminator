__author__ = "Julie Krainer"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Julie Krainer"

import sys
import argparse

parser = argparse.ArgumentParser(description="Deaminates given sequences as fully methylated and fully unmethylated sequence")
parser.add_argument('--input_file', help="File with Sequences. One sequence per row", type=argparse.FileType('r'))

# Date: 01.03.2019

def processRow(file):
    content = file.readlines()
    deaminated = list()
    deaminated.append(["unmeth", "meth"])
    for row in content:
        seq = row.rstrip()
        unmeth = seq.replace("C", "T")
        meth = seq.replace("CG", "XX").replace("C", "T").replace("XX", "CG")
        deaminated.append([unmeth, meth])

    with open("deaminated_sequences.txt", "w") as outfile:
        outfile.writelines('\t'.join(i) + '\n' for i in deaminated)



def main():
    ## Parse the arguments
    args = parser.parse_args()

    ## Get the input file
    input_file = args.input_file

    #file = "input_file.txt"
    processRow(input_file)


if __name__ == "__main__":
    sys.exit(main())
