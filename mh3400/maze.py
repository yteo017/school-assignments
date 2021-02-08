from random import shuffle, randrange, random

MAZE_SIZE = 10

def DFS_search(start_node,end_node):             
    mylist = [start_node]                                   #start with a list with the starting node
    visited = []                                            #create an empty list to store the nodes once they have been visited
    while True:
        current_node = mylist.pop()                         #the current node will be the last element in the list
                                                            #popped out like in a stack because we want last in first out
                                                            #as the neighbours of the current node gets added to the end of the list and we want to get that
        if current_node in visited: continue                #if the node has already been visited, we go back to the top of the loop and find the next current node
                                                            #which either means we have reached a dead end and thus need to backtrack
                                                            #or we just needed to find another neighbour of the previous current node to continue the path
        for node in g[current_node]:                        #run through all nodes that are neighbour to the current node
            mylist.append(node)                             #add it to "mylist"
        visited.append(current_node)                        #add current node to "visited" 
                                                            
        if current_node == end_node:                        #if we reach the ending node, we have found a path, including the extra nodes that do not contribute to the final path
            break 
    
    #visited contains all nodes visited, including those that are not part of the final path
    #thus the next part removes these nodes that do not contribute to the final path
    for i in range(len(visited)):
        if i+1 < len(visited):                              #this ensures we are referencing within the length of "visited", as we constantly update "visited" 
            elem = visited[-i]                              #start from the back
            for j in g[elem]:                               #run through the neighbouring nodes of the respective node
                if j in visited:                            #provided the neighbours are part of "visited"
                    if j != visited[-i-1]:                  #check if the previous node in "visited" is a neighbour of the current node
                        index = visited.index(j)            #if not, take note of the index of the neighbour node with respect to "visited"
                        del visited[index+1:-i]             #so the excess path that does not link the neighbour to the current node can be deleted away
                        
    return visited


def BFS_search(start_node,end_node):
    mylist = [start_node]                                   #start with a list with the starting node
    visited = []                                            #create an empty list to store the nodes once they have been visited
    while True:
        current_node = mylist.pop(0)                        #the current node will be the first element in the list
                                                            #popped out like in a queue, because we want first in first out
                                                            #so that all direct neighbours of the nodes are added before moving on to the neighbours of the neighbours
        if current_node in visited: continue                #if the node has already been visited, we go back to the top of the loop and find the next current node
        for node in g[current_node]:                        #run through all nodes that are neighbour to the current node
            mylist.append(node)                             #add it to "mylist"
        visited.append(current_node)                        #add current node to "visited" 

        if current_node == end_node:                        #if we reach the ending node, we have found a path, including the extra nodes that do not contribute to the final path
            break 
     
    #visited contains all nodes visited, including those that are not part of the final path
    #and for BFS, all the nodes in the maze are in visited as we traversed all to find the shortest path leading to the ending node
    #thus the next part removes these nodes that do not contribute to the final path, which we want to be the shortest
    for i in range(len(visited)):
        if i+1 < len(visited):                              #this ensures we are referencing within the length of "visited", as we constantly update "visited" 
            elem = visited[-i]                              #start from the back
            for j in g[elem]:                               #run through the neighbouring nodes of the respective node
                if j in visited:                            #provided the neighbours are part of "visited"
                    if j != visited[-i-1]:                  #check if the previous node in "visited" is a neighbour of the current node
                        index = visited.index(j)            #if not, take note of the index of the neighbour node with respect to "visited"
                        del visited[index+1:-i]             #so the excess path that does not link the neighbour to the current node can be deleted away
                        
    return visited

 
def make_maze(m_size):
    vis = [[0] * m_size + [1] for _ in range(m_size)] + [[1] * (m_size + 1)]
    ver = [["|:"] * m_size + ['|'] for _ in range(m_size)] + [[]]
    hor = [["+-"] * m_size + ['+'] for _ in range(m_size + 1)]
 
    def walk(x, y):
        vis[y][x] = 1
 
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+ "
            if yy == y: ver[y][max(x, xx)] = " :"
            walk(xx, yy)
 
    walk(randrange(m_size), randrange(m_size))
 
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    
    s_temp = s
    graph = [[] for i in range(MAZE_SIZE*MAZE_SIZE)]
    for col in range(MAZE_SIZE):
        for row in range(MAZE_SIZE):
            if s_temp[(2*row+1)*(2*MAZE_SIZE+2)+(2*col)] == " " or (random() < 1/(2*MAZE_SIZE) and col != 0): 
                graph[col+MAZE_SIZE*row].append(col-1+MAZE_SIZE*row)
                graph[col-1+MAZE_SIZE*row].append(col+MAZE_SIZE*row)
                
            if s_temp[(2*row+2)*(2*MAZE_SIZE+2)+(2*col)+1] == " " or (random() < 1/(2*MAZE_SIZE) and row != MAZE_SIZE-1): 
                graph[col+MAZE_SIZE*row].append(col+MAZE_SIZE*(row+1))
                graph[col+MAZE_SIZE*(row+1)].append(col+MAZE_SIZE*row)
    
    return s,graph
 
   
def print_maze(g, path, players):
      
    s = ""
    for col in range(MAZE_SIZE): s+="+---"
    s+="+\n"
    
    for row in range(MAZE_SIZE): 
        s+="|"
        for col in range(MAZE_SIZE): 
            if row*MAZE_SIZE+col == players[0]: s+="👨 "
            elif row*MAZE_SIZE+col == players[1]: s+="🍒 "
            elif row*MAZE_SIZE+col in path: 
                ind = path.index(row*MAZE_SIZE+col)
                if path[ind+1] == row*MAZE_SIZE+col+1: s+=" → "
                elif path[ind+1] == row*MAZE_SIZE+col-1: s+=" ← "
                elif path[ind+1] == row*MAZE_SIZE+col+MAZE_SIZE: s+=" ↓ "
                elif path[ind+1] == row*MAZE_SIZE+col-MAZE_SIZE: s+=" ↑ "
                else: s+="ppp"
            else: s+="   " 
            if (row*MAZE_SIZE+col+1) in g[row*MAZE_SIZE+col]: s+=" "
            else: s+="|"
                
        s+="\n+" 
        for col in range(MAZE_SIZE): 
            if ((row+1)*MAZE_SIZE+col) in g[row*MAZE_SIZE+col]: s+="   +"
            else: s+="---+"
        s+="\n"
        
        
    print(s)
                
    
    
s, g = make_maze(MAZE_SIZE)    
players = [0,MAZE_SIZE*MAZE_SIZE-1]
print(g)

print("\n\n ******** PERFORMING DFS ********" )
path_DFS = DFS_search(players[0],players[1])
print_maze(g,path_DFS,players)
print("Path length for DFS is %i" % (len(path_DFS)))

print("\n\n ******** PERFORMING BFS ********" )
path_BFS = BFS_search(players[0],players[1])
print_maze(g,path_BFS,players)
print("Path length for BFS is %i" % (len(path_BFS)))