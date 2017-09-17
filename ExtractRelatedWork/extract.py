import sys
import os

# usage [1] filename [2] the name of chap after Related
fname = sys.argv[1]
nxtchap = sys.argv[2]
outfile = 'tmp.txt'
os.system("pdftotext '%s' '%s'" % (fname, "tmp.txt"))

fname = open(outfile, 'r')

def extractNumbers(nums, papers):
    nums = nums.strip()
    numList = nums.split(',')
    for num in numList:
        papers.append(int(num.strip()))


def collectPapers(rw, papers) :
    stacks = ""
    for c in rw:
        if c == ']':
            extractNumbers(stacks, papers)
            stacks = ""
            continue
        if len(stacks) != 0:
            stacks = stacks + c
            continue
        if c == '[': 
            # need to check 
            stacks = stacks + ' '
            continue;

def refStIsLegal(ref):
    # only check the first 5 character
    line = ref.strip()
    line = line[0:5]
    if len(line) == 0:
        return False
    if line[0] != '[':
        return False
    digits = ""
    
    length = len(line)
    length = min(5, length)
    findEnd = False
    for i in range(1, length):
        if line[i] == ']':
            findEnd = True
            break
        digits = digits + line[i]

    if not findEnd:
        return False

    if digits.isdigit():
        return True
    else:
        return False


# locate related work
RelatedWork = ""
papers = [] 
findRW = False
cntnRW = True 
findRF = False
cntnRF = False 

# string list
References = []
title = ""

for line in fname:
    if ('Related Work' in line): findRW = True
    if ('References' in line): findRF = True
    
    if (findRW and cntnRW):
        RelatedWork = RelatedWork + line.strip() + " "
        if nxtchap in line : 
            collectPapers(RelatedWork, papers)
            cntnRW = False
    if (findRF):
        if refStIsLegal(line):
            if cntnRF:
                References.append(title) 
                title = ""
            cntnRF = True
        if cntnRF:
            title = title + line.strip() 

papers = list(set(papers))
for num in papers:
    print (References[num-1])
