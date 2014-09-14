#!/usr/bin/python
import csv
import sys
import os
import re

TOGGLE_EMAIL = 'erbor.iceman@gmail.com'
TOGGLE_PROJECT = 'Project 1'
TOGGLE_TAG = 'zone'
OUTPUT_FILENAME = 'toggl_import.csv'

def parse_file(filename):
    fh = open(filename, 'Ur')
    nfh = open(OUTPUT_FILENAME,'w')
    for line in csv.reader(fh,delimiter=',',skipinitialspace=True):
        col = []
        col=line
        # col 3 is time which is in decimal format. converting it to HH:MM:SS format
        # 2.06 => 02:06:00
        if re.search(r'[0-9]+\.[0-9]+',line[2]):
            modify = float(line[2])
            it = int(modify)
            dec = int(float((modify-it))*60)
            if it<10:
                it = '0'+str(it)
            else:
                it = str(it)

            if dec<10:
                dec = '0'+str(dec)
            else:
                dec = str(dec)
            res = str(it)+":"+str(dec)+":"+"00"
            
            #storing result
            col[2] = res

            # appending custom columns required toggl
            col.append(TOGGLE_PROJECT)
            col.append(TOGGLE_EMAIL)
            col.append(line[0]) #adding Zone description as description for task
            col.append(TOGGLE_TAG)
            col.append('00:00:00')
        else:
            col.append('Project')
            col.append('Email')
            col.append('Description')
            col.append('Tag')
            col.append('Start time')

        nfh.write(','.join(col))
        nfh.write('\n')

    fh.close()
    nfh.close()

    print 'Done. Result stored in file = ' + str(OUTPUT_FILENAME) 
    return


def main():
    filename = ""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print 'Enter filename'
        filename = sys.stdin.readline().rstrip()

    if not os.path.isfile(filename):
        print 'Invalid file path'
        sys.exit(1)

    parse_file(filename)
    return

if __name__ == '__main__':
    main()
