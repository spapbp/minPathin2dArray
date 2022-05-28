import collections

grid = [[0, 0,"S", 0, 0], 
        [0, 0, 0,  0, 0], 
        [0, 0, 0, "E",0]]

q = collections.deque()
q.append([0, 2])

def sol(grid):
    
    moves = 0
    
    # while stack is not empty, still has stuff to look through
    while q:
        
        # look through currently appended layer
        # appending does not increase len
        for i in range(len(q)):
            row, col = q.popleft()
            
            #check if out of bounds
            if row < 0 or row >= len(grid):
                continue
            if col < 0 or col >= len(grid[0]):
                continue
            
            # check if visisted
            if grid[row][col] == 1:
                continue
            
            # check if end
            if grid[row][col] == "E":
                return moves
            
            # mark visited
            grid[row][col] = 1
        
            # add next layer, does not affect for loop runs
            # happens each pop
            q.append([row+1, col])
            q.append([row-1, col])
            q.append([row, col+1])
            q.append([row, col-1])
        
        # one for loop is one layer processed
        moves += 1

print(sol(grid))
