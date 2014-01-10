#!/usr/bin/env python

'rots.py -- find caesar shift pairs in american-english'
'uses dictionary found in /usr/share/dict'

def getpairs():
    pairs = []

    try:
        f = open("/usr/share/dict/american-english", "r")
    except IOError, e:
        print "*** file open error: ", e
    else: 

        strs = f.readlines()
        raw = [x[:-1] for x in strs]
        raw2 = [x.replace("'s", "") for x in raw]
        raw3 = [x for x in raw2 if len(x)>2]
        vocab = set([x.lower() for x in raw3])  
        
        for word in vocab:
            for shift in range(1, 14):
                caesar = "".join([chr(97 + ((ord(x) - 97 + shift) % 26)) for x in word])
                if caesar in vocab:
                    print word, caesar, shift
                    pairs += tuple([word, caesar, shift])

    return len(pairs)

if __name__ == "__main__":
    print getpairs(), "pairs found"
    print "note, each pair has a reverse shift as well"
    
