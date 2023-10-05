from typing import List

import pandas as pd
import numpy as np
import statistics as st

def multLists (lref, lshort, startIdx):
    sz : int = len(lshort)
    sum : float=0.0
    for idx in range(sz):
        sum += lref[idx+startIdx] * lshort[idx] / sz
    return sum
def subLists (lref, lshort, startIdx):
    sz : int = len(lshort)
    sum : float=0.0
    for idx in range(sz):
        sum += (lref[idx+startIdx] - lshort[idx]) / sz
    return sum

def multListsDiffs (lref, lshort, startIdx):
    sz : int = len(lshort)
    sum : float=0.0
    for idx in range(sz):
        mean = (lref[idx+startIdx] + lshort[idx]) / 2.0
        sum += (lref[idx+startIdx] - mean) * (lshort[idx] - mean) / sz
    return sum

def multListsMod (lref, lshort, startIdx):
    sz : int = len(lshort)
    sum : float=0.0
    for idx in range(sz):
        sum += (lref[(idx+startIdx) % sz]) * (lshort[idx]) / sz
    return sum

def corrSeries(ser1, ser2, method : int):
    if method == 1:
        sz = len (ser1)
        sliceSz = int(sz/10)
        slice1 = list(ser1[0:sliceSz])
        slice2 = list(ser2[0:sliceSz])
        paddingl: list[float] = [0.0 for i in range(sliceSz)]
        paddingr: list[float] = [0.0 for i in range(sliceSz)]
        slice1 = paddingl + slice1 + paddingr;
        # slice1 = slice1 + slice1 + slice1
        resl=[]
        for ind in range(sliceSz*2):
            corrRes = multLists(slice1, slice2, ind)
            resl.append(corrRes)
            if not ind % 100:
                print ("ind: {0}\n".format(ind))
        return resl
    if method == 2:
        sz = len (ser1)
        sliceSz = int(sz/100)
        slice1 = [ser1[i] for i in range(sz) if i % sliceSz == 0]
        slice2 = [ser2[i] for i in range(sz) if i % sliceSz == 0]
        actLen = len(slice1)
        paddingl: list[float] = [0.0 for i in range(actLen)]
        paddingr: list[float] = [0.0 for i in range(actLen)]
        slice1 = paddingl + slice1 + paddingr;
        resl=[]
        for ind in range(actLen*2):
            #corrRes = subLists(slice1, slice2, ind)
            #corrRes = multLists(slice1, slice2, ind)
            corrRes = multListsDiffs(slice1, slice2, ind)
            resl.append(corrRes)
            if not ind % 100:
                print ("ind: {0}\n".format(ind))
        midx = resl.index(max(resl))
        print("len: {0} max: {1}\n".format(actLen, midx))
        return resl
    if method == 3:
        sz = len (ser1)
        sliceSz = int(sz/100)
        slice1 = [ser1[i] for i in range(sz) if i % sliceSz == 0]
        slice2 = [ser2[i] for i in range(sz) if i % sliceSz == 0]
        actLen = len(slice1)
        resl=[]
        for ind in range(actLen*2):
            corrRes = multListsMod(slice1, slice2, ind)
            resl.append(corrRes)
            if not ind % 100:
                print ("ind: {0}\n".format(ind))
        midx = resl.index(max(resl))
        print("len: {0} max: {1}\n".format(actLen, midx))
        return resl

