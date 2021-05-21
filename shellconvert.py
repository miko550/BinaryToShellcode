import sys
from typing import Sized

try:
    plaintext = open(sys.argv[1], "rb").read() 
except:
    print("File argument needed! %s <raw payload file>" % sys.argv[0])
    sys.exit()

sc = []
#sc = ", ".join("0x{:2x}".format(c) for c in plaintext)
#sc = ", ".join(hex(x) for x in plaintext)
#sc = '0x' + ', 0x'.join(hex(x)[2:] for x in plaintext)
#"".join("\\x{:02x}".format(c) for c in shellcodesrc)
for x in plaintext:
    sc.append(format(x, '#04x'))

print(', '.join(sc))
print("Bytes length : %s" % len(sc))

print("The hexadecimal form of 23 is "+ hex(0))