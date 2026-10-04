import re, struct, sys
from collections import Counter
runs = []
for line in open(sys.argv[1]):
    m = re.search(r"offset (0x[0-9a-f]+)-(0x[0-9a-f]+)", line)
    if m:
        runs.append((int(m.group(1), 16), int(m.group(2), 16)))
sizes = {}
for a, b in runs:
    sizes.setdefault(b - a, []).append(hex(a))
idx = open("extract/FILE.IDX", "rb").read()
w = struct.unpack("<%dI" % (len(idx) // 4), idx[:len(idx) // 4 * 4])
print("code runs:", len(runs), " idx words:", len(w))
recs = [i for i in range(56, len(w) - 3, 4) if w[i + 2] == 2]
print("records with type 2:", len(recs))
hits = 0
for i in recs:
    s = (w[i + 3] + 0x7ff) & ~0x7ff
    if s in sizes:
        hits += 1
        print("rec word %d: size %#x -> %#x  matches runs at %s" % (i, w[i + 3], s, sizes[s][:3]))
print("records whose size matches a code run:", hits)
print("handlers:", Counter(hex(w[i + 1]) for i in recs).most_common(8))
