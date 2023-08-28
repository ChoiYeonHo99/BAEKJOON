import sys

def compress_video(x: int, y: int, k: int):
    global result
    if check_video(x, y, k):
        result += str(video[x][y])
    else:
        result += "("
        kdot = k // 2
        compress_video(x, y, kdot)
        compress_video(x, y + kdot, kdot)
        compress_video(x + kdot, y, kdot)
        compress_video(x + kdot, y + kdot, kdot)
        result += ")"

def check_video(x: int, y: int, k: int):
    color = video[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if color != video[i][j]:
                return False
    return True
    

n = int(sys.stdin.readline().rstrip())
video = []
result = ""
for _ in range(n):
    line1 = sys.stdin.readline().rstrip()
    line2 = []
    for i in range(n):
        line2.append(int(line1[i]))
    video.append(line2)

compress_video(0, 0, n)
print(result)