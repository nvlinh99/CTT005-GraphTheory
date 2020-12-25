from Graphs import initialize, generateFigure, getRawData, readMatrix, np
from Colors import *
from student_functions import DFS, BFS, UCS
import pygame
from pygame.locals import *
pygame.init()
clock=   pygame.time.Clock()
font =   pygame.font.Font(pygame.font.get_default_font(), 25)
fps = 5  # frames per sec
window = pygame.display.set_mode((800, 600), DOUBLEBUF)
screen = pygame.display.get_surface()

time_delay=None

def drawFig(raw_data, size):
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0,0))
    pygame.display.flip()

def update(G, color_map, pos):
   
    fig = generateFigure(G, color_map, pos)
    raw_data, size= getRawData(fig)
    drawFig(raw_data,size)
    pygame.display.update()
    clock.tick(fps)
    pygame.time.delay(time_delay)

def quit_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()

def searchAnimation(matrix, visited, G, pos, color_map):
    tmp=[]
    for v1, v2 in visited.items():
        cur_node = v1
        queue_nodes = np.where(matrix[cur_node]!=0)[0]
        color_map[cur_node]=current_color
        for node in queue_nodes:
            if node not in tmp:
                color_map[node]=queue_color
        update(G, pos, color_map)
        color_map[cur_node]=visited_color
        tmp.append(cur_node)
        update(G, pos, color_map)

def paintPath(path, G, pos, color_map):
    n_nodes=len(path)
    for i in range(n_nodes):
        node=path[i]
        color_map[node]=path_node_color
        if i< (n_nodes-1):
            G[node][path[i+1]]['color'] = path_color
    update(G, pos, color_map)
def run(input, algorithm, delay):
    global time_delay
    time_delay=delay
    matrix, start, end=readMatrix(input)
    G, pos, color_map=initialize(matrix)
    update(G, pos, color_map)
   
    if algorithm == 'bfs':
        visited, path = BFS(matrix, start, end)
    elif algorithm == 'dfs':
        visited, path = DFS(matrix, start, end)
    elif algorithm == 'ucs':
        visited, path  = UCS(matrix, start, end, pos)
    else:
        print("Pass a search algorithm to run program.")

    searchAnimation(matrix, visited, G, pos, color_map)
    paintPath(path, G, pos, color_map)
    while True:
        quit_event()
    


    

