import sys

rainbowDance = {"ChongChong"}
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    meetting = sys.stdin.readline().rstrip().split()
    if meetting[0] in rainbowDance or meetting[1] in rainbowDance:
        rainbowDance.add(meetting[0])
        rainbowDance.add(meetting[1])

count = len(rainbowDance)
print(count)