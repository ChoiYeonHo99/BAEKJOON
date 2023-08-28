import sys

def hanoi(n, from_pos, to_pos, aux_pos):
    global count
    if n == 1:
        count += 1
        move.append((from_pos, to_pos))
        return
    
    hanoi(n-1, from_pos, aux_pos, to_pos)
    count += 1
    move.append((from_pos, to_pos))
    hanoi(n-1, aux_pos, to_pos, from_pos)

global count, move
count = 0
move = []

n = int(sys.stdin.readline().strip())
hanoi(n, 1, 3, 2)
print(count)
for i in range(0, count):
    print(move[i][0], move[i][1])