import filecmp
import os
test_res= os.system('python3 frequentwords.py --mainfile b-test1.txt --file2 b-test2.txt > b-test-r.txt')


if(filecmp.cmp('b-test-r-correct.txt', 'b-test-r.txt')):
    print("Test: PASSED")
else:
    print("Test: FAILED")
