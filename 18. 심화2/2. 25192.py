import sys

chatLog = []
count = 0
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    name = sys.stdin.readline().rstrip()
    if name == "ENTER":
        gomgom = set(chatLog)
        count += len(gomgom)
        chatLog = []
    else:
        chatLog.append(name)

gomgom = set(chatLog)
count += len(gomgom)
print(count)