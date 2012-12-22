#!/usr/bin/env python2.6
#
# [The "New BSD" license]
# Copyright (c) 2012 The Board of Trustees of The University of Alabama
# All rights reserved.
#
# See LICENSE for details.

from __future__ import print_function

import os


# order preserving uniq for lists
def _uniq(L):
    seen = {}
    result = []
    for item in L:
        if item in seen:
            continue
        seen[item] = 1
        result.append(item)
    return result


# exception handling mkdir -p
def _make_dir(dir):
    try:
        os.makedirs(dir)
    except os.error as e:
        if 17 == e.errno:
            # the directory already exists
            pass
        else:
            print('Failed to create "%s" directory!' % dir)
            sys.exit(e.errno)


# file line length
def _file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

# find all indices of a list of strings that match a regex
def findall_regex(l, r):
    found = list()
    for i in range(0, len(l)):
        k = r.match(l[i])
        if k:
            found.append(i)
            k = None

    return found

def split_by_regex(l, r):
    splits = list()
    indices = findall_regex(l, r)
    k = None
    for i in indices:
        if k is None:
            splits.append(l[0:i])
            k = i
        else:
            splits.append(l[k:i])
            k = i

    splits.append(l[k:])

    return splits

