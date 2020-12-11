from ortools.sat.python import cp_model
from random import randrange
import os
import sys
import json

from tile_info import create_adjacency_mappings

model = cp_model.CpModel()
solver = cp_model.CpSolver()

adjacency_mappings = create_adjacency_mappings()
# print(json.dumps(adjacency_mappings, indent=2,))

width = 0
height = 0
while True: 
    try: 
        
        width = int(input("What is your desired width? "))
        height = int(input("What is your desired height? "))
    except NameError: 
        print("Not a number! Try again")
    except ValueError: 
        print("Not a number! Try again")
    except SyntaxError: 
        print("Not a number! Try again")

    
    else: 
        if width < 5: 
            print("Width must be greater than 4. Let's try again.")
        elif height < 5: 
            print("Height must be greater than 4. Let's try again.")
        else: 
            break

# add 2 for borders
width += 2
height += 2

num_tiles = len(adjacency_mappings)
grid = {}

# Create grid
for i in range(width):
    for j in range(height):
        for k in range(num_tiles):
            # grid[i,j,k] = model.NewBoolVar(f"[{i},{j}]:{k}")
            grid[i,j,k] = model.NewBoolVar("[%s, %s]: %s" % (i, j, k))

# Exactly one true boolean per 2D grid space
for i in range(width):
    for j in range(height):
        model.Add(sum([grid[i,j,k] for k in range(num_tiles)]) == 1)

# All adjacent tile constraints
for i in range(width):
    for j in range(height):
        for k in range(num_tiles):
            # For each adjacent position
            for index, (i2, j2) in enumerate([(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]):
                # If adjacent position is inside the grid
                if i2 >= 0 and i2 < width and j2 >= 0 and j2 < height:
                    model.AddBoolOr([grid[i2, j2, k2] for k2 in adjacency_mappings[k]["neighbors"][index]]).OnlyEnforceIf(grid[i, j, k])

# Limit Number of Tile
def limit_tile_type(tile_base_num, limit):
        model.Add(sum(grid[i,j,k]
            for i in range(width)
            for j in range(height)
            for k in range(tile_base_num, tile_base_num + 4)
        ) <= limit)

# Limit Doors
limit_tile_type(16, 8)

# Limit outside wall corners
limit_tile_type(12, 16)

# General limit
# max_num_of_each_tile = width * height / num_tiles * 2
max_num_of_each_tile = 60
[limit_tile_type(k, max_num_of_each_tile) for k in range(0, num_tiles, 4) if k not in [8,16,20,24]]

# Add borders
model.Add(grid[0,0,24] == True)
model.Add(grid[0, height - 1, 24] == True)
model.Add(grid[width - 1, 0, 24] == True)
model.Add(grid[width - 1, height - 1, 24] == True)
model.Add(grid[5,0,20] == True)
for i in range(1, width - 1):
    model.Add(grid[i, 0, 20] == True)
    model.Add(grid[i, height-1, 22] == True)
for j in range(1, height - 1):
    model.Add(grid[0, j, 21] == True)
    model.Add(grid[width - 1, j, 23] == True)

# To break symmetry
for i in range(7):
    model.AddHint(grid[randrange(1, width - 1), randrange(1, height - 1), randrange(0, num_tiles)], True)

if solver.Solve(model) in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    file_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0] + "/Assets/Layouts/layout.txt"
    file = open(file_path, "w")
    for j in range(height): 
    # for i in range(width):
        line = ""
        for i in range(width): 
        # for j in range(height):
            for k in range(num_tiles):
                if solver.Value(grid[i,j,k]) == 1:
                    # line += f"{k}"
                    line += "%s" % (k)
                    if i < width - 1: 
                    # if j < height - 1:
                        line += " "
                    else:
                        line += "\n"
        # print(line)
        file.write(line)
    file.close()
    print("New Layout Created!")
else:
    print("Not Feasible")