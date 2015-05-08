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


        except FileNotFoundError:
            print('Error: File not found ;/')


def main():
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " <the_file.csv>")
        exit(1)
    else:
        threeOhOne = ThreeOhOne(sys.argv[1])

if __name__ == "__main__":
    main()
