import sys
sys.path.append('./testcase')
sys.path.append('./lib')
from case import case

# run all testcases
for run_case in case:
    run_case()
