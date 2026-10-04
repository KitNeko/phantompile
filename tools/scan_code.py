import sys
d = open(sys.argv[1], "rb").read()
SEC = 2048
pat = bytes.fromhex("0800e003")
hits = [0] * (len(d) // SEC + 2)
i = d.find(pat)
while i != -1:
    if i % 4 == 0:
        hits[i // SEC] += 1
    i = d.find(pat, i + 1)
start = None
for i, n in enumerate(hits):
    if n and start is None:
        start = i
    if not n and start is not None:
        if i - start >= 4:
            print(f"sectors {start}-{i-1}  offset {start*SEC:#x}-{i*SEC:#x}  size {(i-start)*SEC:#x}  jr_ra={sum(hits[start:i])}")
        start = None
