#!/usr/bin/python

## pwd215.py - Compute a PWD
##
## Written in 2016 by Vitorio Miliano
##
## To the extent possible under law, the author has dedicated all
## copyright and related and neighboring rights to this software to
## the public domain worldwide.  This software is distributed without
## any warranty.
##
## You should have received a copy of the CC0 Public Domain
## Dedication along with this software.  If not, see
## <http://creativecommons.org/publicdomain/zero/1.0/>.

import os, re, sys

uidre = re.compile('^04[0-9a-f]{12}$', re.IGNORECASE)

def calc_keya(uid, sector):
    if uidre.match(uid) is None:
        raise ValueError('invalid UID (seven hex bytes)')

    if sector < 0 or sector > 134:
        raise ValueError('invalid sector (0-134)')

    intvals = [int(uid[i] + uid[i+1], 16) for i in range(0, len(uid), 2)]
    
    intkey = [intvals[1] ^ intvals[3] ^ 170, intvals[2] ^ intvals[4] ^ 85, intvals[3] ^ intvals[5] ^ 170, intvals[4] ^ intvals[6] ^ 85]
    
    key = ''.join(format(i, '02x') for i in intkey)
    return key

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print calc_keya(sys.argv[1], 0)
