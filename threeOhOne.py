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
import re
import urllib.request

class ThreeOhOne:
    outputDir = 'outputs/'
    csvHeadings = ['404 URLs', 'New URL', 'Redirect']

    def __init__(self, filename):
        self._process(sys.argv[1])

    def _process(self, filename):
        try:
            fd = open(filename, 'rt')
        except FileNotFoundError as err:
            print('Error: File not found ;/ ({0})'.format(err))

        try:
            fdOut = open(self.outputDir + filename + '.out.csv', 'w')
            writer = csv.writer(fdOut, delimiter=',')
            processedRows = []

            reader = csv.reader(fd)
            for row in reader:
                if self.csvHeadings[0] not in row:
                    newRow = []
                    i = 1

                    for column in row:
                        if i == 2:
                            column = column.replace('www.', '')
                        elif i == 3:
                            # if re.search('^Redirect', column):
                            columnPieces = re.split('\s{1}', column)

                            columnPieces[2] = urllib.request.unquote(columnPieces[2])
                            columnPieces[3] = urllib.request.unquote(columnPieces[3])

                            if ' ' in columnPieces[2]:
                                columnPieces[2] = '"' + columnPieces[2] + '"'
                            if ' ' in columnPieces[3]:
                                columnPieces[3] = '"' + columnPieces[3] + '"'

                            column = ' '.join(columnPieces)
                        else:
                            column = urllib.request.unquote(column)
                            if ' ' in column:
                                column = '"' + column + '"'

                        newRow.append(column)
                        i = i + 1
                    processedRows.append(newRow)

            writer.writerows(processedRows)
            fdOut.close()
        except:
            print('Error:', sys.exc_info()[0])
            raise

        fd.close()


def main():
    if len(sys.argv) < 2:
        print("usage: " + sys.argv[0] + " <the_file.csv>")
        exit(1)
    else:
        threeOhOne = ThreeOhOne(sys.argv[1])

if __name__ == "__main__":
    main()
