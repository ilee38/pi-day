#!/usr/bin/env python3

from decimal import Decimal as Dec, getcontext as gc

# Parameter defaults chosen to gain 1000+ digits within a few seconds
def PI(maxK = 317, prec = 15001, disp = 15000):
    gc().prec = prec
    K, M, L, X, S = 6, 1, 13591409, 1, 13591409
    for k in range(1, maxK + 1):
        M = (K**3 - 16*K) * M // k**3
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
        K += 12
    pi = 426880 * Dec(10005).sqrt() / S
    # Drop a few digits of precision for accuracy
    pi = Dec(str(pi)[:disp])
    return pi


def main():
  pi = PI()
  print(pi)


if __name__ == '__main__':
  main()
