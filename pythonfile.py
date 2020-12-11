import sys
from ortools.sat.python import cp_model

arg1 = sys.argv[1]
# arg2 = sys.argv[2]

outFile = open("test.txt", "w")
outFile.write(arg1)
outFile.close()
