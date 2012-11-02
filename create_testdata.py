'''
Created on 1 Nov 2012

@author: flynns
'''

import os
import random
import time

num_level1_dirs = 5
num_level2_dirs = 5
num_files = 10000

root = r'C:\Documents and Settings\flynns\Desktop\testdata'
howmany = 0

start = time.time()
for feed in range(0, num_level1_dirs):
    # print ("Create Feed directory", feed)
    for batch in range(0, num_level2_dirs):
        # print ("Create Batch directory", batch)
        for file in range(0, num_files):
            os.makedirs(root + "\F" + str(feed) + "\B" + str(batch), exist_ok=True)
            os.chdir(root + "\F" + str(feed) + "\B" + str(batch))
            if random.random() > 0.5:
                suffix = ".txt"
            else:
                suffix = ".xml"
            filename = "file_" + str(file) + suffix
            output = open(filename, mode='w')
            output.write("This is some file contents")
            # output.close
            howmany += 1
            if howmany % 500 == 0:
                end = time.time()
                print (howmany, end - start)
                start = end

if __name__ == '__main__':
    pass
