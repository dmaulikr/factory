#!/usr/bin/env python


# Resource Converter
#
# Converts a resource output generated by the DeRez tool and focuses on 
# 8img and 4img resource forks, outputting them to RAW image files
#
# Taylan Pince (taylanpince at gmail dot com)


import os
import sys

from binascii import a2b_hex
from math import ceil
from optparse import OptionParser


def main():
    parser = OptionParser(usage="Usage: %prog [options] --file=FILE_PATH", version="%prog 0.1")

    parser.set_defaults(output_dir=os.getcwd())
    parser.add_option("-f", "--file", dest="file_path", help="Path to the resource file to parse")
    parser.add_option("-o", "--output-dir", dest="output_dir", help="Output path, by default the current working directory")

    (options, args) = parser.parse_args()
    
    if not options.file_path:
        parser.error("You have to specify a file path")

    file = open(options.file_path, "r")
    output = None
    count = 0

    for line in file.readlines():
        if output is not None and "};" in line:
            # output.close()
            # output = None
            break
        elif "4img" in line:
            # output = open(os.path.join(options.output_dir, "%s.raw" % line[line.find("(") + 1:line.find(")")]), "wb")
            output = ""
        elif output is not None:
            code = line[line.find('"') + 1:line.find('"', line.find('"') + 1)].replace(" ", "")

            for i in range(0, int(ceil(len(code) / 2))):
                count += 1
                output += "%03d " % int(code[i * 2:i * 2 + 2], 16)

                if count == 16:
                    print output
                    count = 0
                    output = ""
            # for i in range(0, len(code)):
            #     count += 1
            #     output += "%03d " % int(code[i:i + 1], 16)
            # 
            #     if count == 24:
            #         print output
            #         count = 0
            #         output = ""
                # bit = code[i:i + 1]
                # print bit, int(bit, 16)
                # output.write(a2b_hex(bit))
                # output.write(a2b_hex("%s%s" % (bit, bit)))  
                # print code[bit * 2:bit * 2 + 2], int(code[bit * 2:bit * 2 + 2], 16)

    file.close()


if __name__ == "__main__":
    main()
