import os, os.path
import glob
import sys
from pathlib import Path
inp_file = sys.argv[1]

with open(inp_file) as in_p:
    out_p = open('res_'+inp_file, 'w')
    lines = in_p.readlines() 
    for line in lines:
        line = line.strip()
        try:
            ncCounter = [f for f in os.listdir(line) if f.endswith('.nc')]
        except Exception as e:
            print(e)
        if len(ncCounter) == 1:
            out_p.write(line) 
        else:
            out_p.write('\''+line+'\'')
        out_p.write('\n')
