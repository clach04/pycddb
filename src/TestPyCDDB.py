#!/usr/bin/python

import os
import PyCDDB
import sys

# multiple matches
multiple = "E512640F 15 150 23780 56867 73962 96577 124515 141320 156755 178960 204585 236400 259287 289755 315007 338777 4710"

# exact match
exact1 = "610ADF09 9 150 25620 49322 78800 100775 125492 154060 174270 189407 2785"
exact2 = "760D8B0A 10 150 32087 55987 85822 113087 142505 159912 183780 204622 228625 3469"

# long title
longtitle = "A507FD0E 14 150 13694 20250 31112 44578 54994 66087 75909 88501 98088 108243 116112 132029 143056 2047"

longtrack = "FD096E14 20 150 7337 18658 27494 37765 46752 56217 66153 78005 83493 92709 102300 110874 120177 130618 145099 152388 155617 164602 169465 2416"

# no match
nomatch = "82096E09 9 150 5845 18944 49318 73204 92959 112434 134294 154710 2416"

# read id from compact disc
#f = os.popen("./discid.exe")
#discid = f.readline()
#f.close()

discid = longtrack

db = PyCDDB.PyCDDB()
items = db.query(discid)
if len(items) > 0: # Items found?
    print items
    if (len(items) > 1): # Multiple matches
        print "Multiple matches found. Choose one of:"
        for item in range(len(items)):
            print "%d : %s %s" % (item, items[item]['category'], items[item]['title'])
        index = input("which item?")
    else: # single match
        index = 0

    info = db.read(items[index])
    print info
    if len(info['TTITLE']) > 0: # read info
        print 40 * '-'
        print "Title: %s" % info['DTITLE']
        for track in range(len(info['TTITLE'])):
            print "Track: %02d %s" % (track, info['TTITLE'][track])
        print 40 * '-'
    else:
        print >> sys.stderr, "Read-Status %d: '%s.'" % (db.status(), db.message())
else:
    print >> sys.stderr, "Query-Status %d: '%s.'" % (db.status(), db.message())
