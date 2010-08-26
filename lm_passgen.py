#!/usr/bin/env python

import sys
import string

argument=sys.argv[1]
length=len(argument)

masterlist=[argument.lower()]
print masterlist[0]

for word in masterlist:
    array=list(word)
    position=0
    while position < length:
        if array[position].isalpha():
            if array[position].isupper():
                array[position]=array[position].lower()
                word="".join(array)
                if word not in masterlist:
                    masterlist.append(word)
                    print word
                position += 1
            else:
                array[position]=array[position].upper()
                word="".join(array)
                if word not in masterlist:
                    masterlist.append(word)
                    print word
                position += 1
        else: position +=1