import sys

USAGE = "exo2.py NUMBER"

if len(sys.argv) !=2:
    print(USAGE)
    exit()

try:
    n = int(sys.argv[1])
except:
    print(USAGE)
    exit()


for i in range(n):
    print("$" * i)
