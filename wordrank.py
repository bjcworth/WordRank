import sys

def rank(s):
    '''Return 1-based rank'''

    #list() returns in list format each letter of s
    return rank2(list(s)) + 1


def rank2(s):
    '''Return 0-based rank'''

    if len(s) < 2: return 0

    ordered = s[:]
    ordered.sort()

    d = 1

    # accounting for multiple occurrences of letters
    # enumerate() assigns a numerical value to each letter in ordered
    for x, y in enumerate(ordered):
        n = 1
        while x + n < len(ordered) and ordered[x + n] == y:
            n += 1

        d *= n

    # start alphebatizing before current letter
    pos = ordered.index(s[0])

    # recurse list without head
    return fact(len(s) - 1) * pos / d + rank2(s[1:])

def fact(n):
    ''' return n!'''

    f = 1

    while n > 1:
         f *= n
         n -= 1

    return f

s = sys.argv[1]

print s, rank(s)
