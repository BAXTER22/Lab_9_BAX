# Adjacency matrix for the graph
# 1 is where there is an edge
# 0 is no edge
adj_matrix = [
    [0, 0, 1, 1, 0],  # A 
    [0, 0, 1, 0, 1],  # G
    [1, 1, 0, 1, 0],  # C
    [1, 0, 1, 0, 1],  # T
    [0, 1, 0, 1, 0]   # H
]

vertices = ['A', 'G', 'C', 'T', 'H']


def find_degree(vertex):
    """Find the degree of a vertex."""
    idx = vertices.index(vertex)    # find position
    degree = sum(adj_matrix[idx]) # count 1s
    return degree


def find_neighborhood(vertex):
    """Find all neighbors of a vertex."""
    idx = vertices.index(vertex) # position
    neighbors = []
    for i in range(len(vertices)): # loop thru all vertices, 1s are neighbors
        if adj_matrix[idx][i] == 1:
            neighbors.append(vertices[i])
    return neighbors


def find_path(source, destination):
    """Find a path between two vertices."""
    if source == destination:
        return [source]
    
    neighbors = find_neighborhood(source)
    for neighbor in neighbors:  # find all the neighbors to check if any are the dest
        if neighbor == destination: # direct path
            return [source, neighbor]
    
    return None


# Main program
while True:
    print('\nChoose an action from the menu:')
    print('1. Find degree')
    print('2. Find neighborhood')
    print('3. Find path')
    
    choice = input('Enter your input: ')
    
    if choice == '1':
        vertex = input('Enter the vertex whose degree you want to find: ')
        print('The degree is', find_degree(vertex))  # Removed curly braces
    
    elif choice == '2':
        vertex = input('Enter the vertex whose neighborhood you want to find: ')
        neighbors = find_neighborhood(vertex)
        print('The neighborhood is', set(neighbors))
    
    elif choice == '3':
        source = input('Enter source vertex: ')
        destination = input('Enter destination vertex: ')
        path = find_path(source, destination)
        if path:
            print('A possible path is', path)
        else:
            print('No direct path found')
    
    cont = input('Do you want to continue (Y or N): ')
    if cont != 'Y':  
        print('Goodbye!')
        break


