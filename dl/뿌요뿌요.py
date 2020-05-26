def down():
    for i in marr:
        print(*i)
    print()
    for y in range(N-1, -1, -1):
        for x in range(M):
            if marr[y][x] == '.':
                ny = y-1
                while ny != -1:
                    if marr[ny][x] == '.':
                        ny -= 1
                    else:
                        marr[ny][x], marr[y][x] = marr[y][x], marr[ny][x]
                        break

    check()





def check():
    global result
    visit = [[0] * M for _ in range(N)]
    flag = 0
    for y in range(N):
        for x in range(M):
            if marr[y][x] != '.' and visit[y][x] == 0:
                color = marr[y][x]
                q = [(y, x)]
                match = [(y, x)]
                visit[y][x] = 1
                while q:
                    y, x = q.pop(0)
                    for i in range(4):
                        ny = dy[i] + y
                        nx = dx[i] + x
                        if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
                        if marr[ny][nx] == color:
                            if visit[ny][nx] == 1: continue
                            q.append((ny, nx))
                            match.append((ny, nx))
                            visit[ny][nx] = 1
                if len(match) >= 4:
                    for i in match:
                        marr[i[0]][i[1]] = '.'
                    flag = 1
    if flag == 1:
        result += 1
        down()

N, M = 12, 6
marr = [list(input()) for _ in range(N)]
result = 0
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
# print(marr)
check()
print(result)