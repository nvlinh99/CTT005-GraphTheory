from Graphs import initialize, generateFigure, getRawData, readMatrix, np
from Colors import *
from student_functions import *
import pygame
from pygame.locals import *
pygame.init()
clock=   pygame.time.Clock()
font =   pygame.font.Font(pygame.font.get_default_font(), 25)
fps = 5  # frames per sec
window = pygame.display.set_mode((1024, 768), DOUBLEBUF)
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

def circle(edges, G, pos, color_map):
    for e in edges:
        node_a=e[0]
        node_b=e[1]
        color_map[node_a]=path_node_color
        color_map[node_b]=path_node_color
        G[node_a][node_b]['color'] = path_color
        update(G, pos, color_map)
def run(input, algorithm, delay):
    global time_delay
    time_delay=delay
    matrix,s, t=readMatrix(input)
    G, pos, color_map=initialize(matrix)
    update(G, pos, color_map)
   
    path=None
    if algorithm == 'fordfulkerson':
         flow_matrix, max_flow = FordFulkerson(matrix, s, t)
   
    else:
        print("Pass a search algorithm to run program.")

    G, pos, color_map=initialize(flow_matrix, edge_color=path_color, node_color=path_node_color)
    update(G, pos, color_map)
    while True:
        quit_event()
    


    

