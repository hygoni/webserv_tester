import sys
import os
sys.path.append('./testcase')
from case import case

# run all testcases
for run_case in case:
    run_case()
