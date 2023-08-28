import sys

def cantor(line: list, start, end):
    if end - start >= 3:
        midStart = start + (end - start) // 3
        midEnd = midStart + (end - start) // 3
        for i in range(midStart, midEnd):
            line[i] = " "
        cantor(line, start, midStart)
        cantor(line, midEnd, end)

while True:
    try:
        n = int(sys.stdin.readline().strip())
        line = ["-"] * (3 ** n)
        cantor(line, 0, len(line))
        string = ''.join(str(s) for s in line)
        print(string)
    except ValueError:
        break