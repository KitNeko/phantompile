import struct, sys
d = open(sys.argv[1], "rb").read()
print("file size  :", hex(len(d)))
print("first bytes:", d[:16])
if d[:8] != b"PS-X EXE":
    print("not a PS-X EXE")
    sys.exit(0)
pc, gp, text_addr, text_size = struct.unpack_from("<IIII", d, 0x10)
sp = struct.unpack_from("<I", d, 0x30)[0]
print(f"initial PC : {pc:#010x}")
print(f"gp         : {gp:#010x}")
print(f"load addr  : {text_addr:#010x}")
print(f"text size  : {text_size:#x}")
print(f"stack ptr  : {sp:#010x}")
