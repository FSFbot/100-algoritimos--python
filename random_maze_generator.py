import random

def DrawMaze(width, height):
    # The array that will hold the maze data
    maze = [['wall' for x in range(2*width+1)] for y in range(2*height+1)]

    # Start with a grid of cells, all of which are initially unvisited
    visited = [[0 for x in range(width)] for y in range(height)]
    # Choose a random cell as the current cell and mark it as visited
    stack = [(random.randint(0, width-1), random.randint(0, height-1))]

    while stack:
        x, y = stack[-1]
        visited[y][x] = 1
        maze[2*y+1][2*x+1] = 'cell'

        # Find all unvisited neighbours
        neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        neighbours = [(x, y) for x, y in neighbours if 0 <= x < width and 0 <= y < height and visited[y][x] == 0]

        if neighbours:
            # Choose a random unvisited neighbour and remove the wall to it
            dx, dy = random.choice(neighbours)
            maze[2*y+1+dy-y][2*x+1+dx-x] = 'cell'
            stack.append((dx, dy))
        else:
            # If there are no unvisited neighbours, backtrack
            stack.pop()

    # Print the maze
    for row in maze:
        for cell in row:
            if cell == 'wall':
                print('+', end='')
            else:
                print(' ', end='')
        print()

print(DrawMaze(5,7))