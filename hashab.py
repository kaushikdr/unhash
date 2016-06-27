import sys
# import pdb
def unhash(hash):
    # pdb.set_trace()
    letters = "acdegilmnoprstuw"
    ind = []
    while (hash>37):
        ind.append(hash % 37)
        hash/=37

    unval=""
    for ji in xrange(len(ind)-1,-1,-1):
        try:
            unval += letters[ind[ji]]
        except IndexError:
            return 'Invalid input'
    return unval

try:
    inp = int(sys.argv[1])
except IndexError:
    print 'Please provide an input as an argument.'
print unhash(inp)
