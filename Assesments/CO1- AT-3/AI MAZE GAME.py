import pygame
from collections import deque

pygame.init()

WIDTH, HEIGHT = 500, 500
ROWS, COLS = 10, 10
SIZE = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Maze Escape")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

maze = [
[0,0,1,0,0,0,1,0,0,0],
[1,0,1,0,1,0,1,0,1,0],
[1,0,0,0,1,0,0,0,1,0],
[1,1,1,0,1,1,1,0,1,0],
[0,0,0,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,1,0],
[0,0,0,0,0,0,1,0,1,0],
[1,1,1,1,1,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,0],
[0,1,1,0,0,0,0,0,0,0]
]

start = (0,0)
goal = (9,9)

def bfs():
    q = deque([start])
    parent = {}
    visited = {start}

    while q:
        x, y = q.popleft()
        if (x,y) == goal:
            path = []
            while (x,y) != start:
                path.append((x,y))
                x,y = parent[(x,y)]
            path.append(start)
            return path[::-1]

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = x+dx,y+dy
            if 0<=nx<10 and 0<=ny<10:
                if maze[nx][ny]==0 and (nx,ny) not in visited:
                    visited.add((nx,ny))
                    parent[(nx,ny)] = (x,y)
                    q.append((nx,ny))
    return []

path = bfs()

running = True
step = 0

while running:
    pygame.time.delay(300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    for i in range(ROWS):
        for j in range(COLS):
            color = WHITE
            if maze[i][j] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, (j*SIZE, i*SIZE, SIZE, SIZE))
            pygame.draw.rect(screen, BLUE, (j*SIZE, i*SIZE, SIZE, SIZE),1)

    pygame.draw.rect(screen, GREEN, (start[1]*SIZE,start[0]*SIZE,SIZE,SIZE))
    pygame.draw.rect(screen, RED, (goal[1]*SIZE,goal[0]*SIZE,SIZE,SIZE))

    for i in range(min(step,len(path))):
        x,y = path[i]
        pygame.draw.circle(screen, YELLOW,
                           (y*SIZE+SIZE//2, x*SIZE+SIZE//2), 10)

    if step < len(path):
        step += 1

    pygame.display.update()

pygame.quit()
