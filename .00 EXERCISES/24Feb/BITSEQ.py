import sys
sys.stdin = open("BITSEQ.inp", 'r')
with open("BITSEQ.out", 'w') as f:
    n = int(input())
    a = list(map(int, input().split()))
    
    b = [index for (index, item) in enumerate(a) if item == 0]
    m = a.count(1)
    for length in range(b[-1]+1-b[0], 1, -1):
        for start in range(b[0], b[-1]+1-b[0] - length):
            t= a[start : start+length].count(0) + a[0:start].count(1) + a[start + length : -1].count(1)
            if t > m:
                m = t
    
    out = str(m)
    f.write(out)
