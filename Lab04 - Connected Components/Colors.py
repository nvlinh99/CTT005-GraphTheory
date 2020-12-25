import random
#color
default_color = 'grey'
current_color = 'orange'
visited_color = 'deepskyblue'
path_node_color = 'lime'
queue_color='violet'
path_color = 'red'
dep_color='lightgreen'
des_color='lightgreen'


def random_color():
    r = lambda: random.randint(0,255)
    return '#%02x%02x%02x' % (r(),r(),r())
