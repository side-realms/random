import random
import sys
import ctypes

# https://developer.classpath.org/doc/java/util/Random-source.html
multiplier = 0x5DEECE66D
addend = 0xB
mask = (1 << 48) - 1
BIT_LEN = 48

def make_seed(prv, nxt, bits):
    brute = pow(2, 48-bits) # ブルートフォースする分
    for i in range(brute):
        ttt = (prv << (48-bits)) + i # 仮の mask(ttt) があった場合の prv
        ttt_all = ((ttt*multiplier + addend) & mask) # next の計算内容を再現
        ttt = ttt_all >> (48-bits) # 実際に取り出された分
        if(ttt == nxt):
            return ttt, ttt_all

def nxt_seed(seed, bits):
    seed = (seed*multiplier+addend) & mask
    return seed >> (48-bits)

def nxt_all_seed(seed):
    seed = (seed*multiplier+addend) & mask
    return seed

ans = []

ttt, ttt_all = make_seed(711066753, 652137470, 32)

for i in range(100):
    ans.append(nxt_seed(ttt_all, 32))
    ttt_all = nxt_all_seed(ttt_all)

print("ans: " + str(ans))
