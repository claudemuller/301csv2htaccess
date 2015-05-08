#!/usr/bin/env python
# -*- Coding: utf-8 -*-

"""
" In its present form, it simply takes a comma delimited .csv file and outputs a .txt file containing valid 301 redirect statements for an .htaccess file
"
" author: Claude Müller
" wbsite: http://mediarocket.co.za
"
"""

import sys
import csv

class ThreeOhOne:
    outputDir = 'outputs'

    def __init__(self, filename):
        self._process(sys.argv[1])

    def _process(self, filename):
        try:
            fd = open(filename, 'rt')

            fdOut = open(self.outputDir + filename + '.out.txt', 'w')


            fd.close()
            fdOut.close()
        except FileNotFoundError as err:
            print('Error: File not found ;/ ({0})'.format(err))
        except:
            print('Error:', sys.exc_info()[0])
            raise


def main():
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " <the_file.csv>")
        exit(1)
    else:
        threeOhOne = ThreeOhOne(sys.argv[1])

if __name__ == "__main__":
    main()
