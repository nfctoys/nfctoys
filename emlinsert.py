#!/usr/bin/python

## emlinsert.py - Insert hex data into other hex data
##
## Written in 2018 by Vitorio Miliano
##
## To the extent possible under law, the author has dedicated all
## copyright and related and neighboring rights to this software to
## the public domain worldwide.  This software is distributed without
## any warranty.
##
## You should have received a copy of the CC0 Public Domain
## Dedication along with this software.  If not, see
## <http://creativecommons.org/publicdomain/zero/1.0/>.

import os, sys

if __name__ == '__main__':
    if not len(sys.argv) > 2:
        raise ValueError('usage: {} MFDFILE DATAFILE'.format(sys.argv[0]))
    
    if not os.path.exists(sys.argv[1]) or not os.path.exists(sys.argv[2]):
        raise ValueError('usage: {} MFDFILE DATAFILE'.format(sys.argv[0]))
    
    MFDFILE = []
    with open(sys.argv[1]) as f:
        for line in f:
            MFDFILE.append(line)
    
    DATAFILE = []
    with open(sys.argv[2]) as f:
        for line in f:
            DATAFILE.append(line)
    
    blocks = [x for x in range(4, len(MFDFILE)) if (x+1) % 4]
    
    NEWHEX = []
    b = 0
    for idx, x in enumerate(MFDFILE):
        if idx in blocks:
            if b < len(DATAFILE):
                NEWHEX.append(DATAFILE[b].strip() + (32-len(DATAFILE[b].strip()))*'0' + '\n')
            else:
                NEWHEX.append('0'*32+'\n')
            b = b + 1
        else:
            NEWHEX.append(x)
    
    print ''.join(NEWHEX).strip()

