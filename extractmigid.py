'''
Created on 17 Oct 2012

@author: flynns
'''
import os
import argparse
import time

parser = argparse.ArgumentParser(description='Extracts the migration id from all of the xml files produced by an Optimus run.')
parser.add_argument('-i', '--root', required=True, dest='root')
parser.add_argument('-o', '--outfile', required=False, dest='outfile')
parser.add_argument('-d', '--dropno', required=True, dest='drop_no')
options = parser.parse_args()

if options.outfile != None:
    output = open(options.outfile, mode='w')
else:
    output = ""

howmany = 0
start = time.time()

for r, d, f in os.walk(options.root):
#    print ("Processing XML files in", r)
    for files in f:
        if files.endswith(".xml"):
            howmany += 1
            filename = os.path.join(r, files)
#            try:
            contents = open(filename, "r", encoding="utf-8").readlines()
#            except ValueError:
#                print("Problem reading", filename, "(character set issue?)")
            for line in contents:
                if "<MIGRATION_ID>" in line:
                    migid = line.strip()
                    migid = migid.lstrip('<MIGRATION_ID>')
                    migid = migid.rstrip("</MIGRATION_ID>")
                    sqlstatement = "Insert into image_validation(drop_no,mig_id) values(" + options.drop_no + "'" + migid + "'" + ");\n"
                    if output:
                        output.write(sqlstatement)
                    else:
                        print(sqlstatement)
            if howmany % 500 == 0:
                end = time.time()
                print ("Processing", howmany / (end - start), "per second")

print("Took", end - start, "seconds in total to process", howmany, "xml files")

if __name__ == '__main__':
    pass
