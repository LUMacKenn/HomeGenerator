from ortools.sat.python import cp_model
import json

from tile_info import create_adjacency_mappings

model = cp_model.CpModel()
solver = cp_model.CpSolver()

adjacency_mappings = create_adjacency_mappings()
print(json.dumps(adjacency_mappings, indent=2,))

width = 10
height = 10
num_tiles = len(adjacency_mappings)
grid = {}

# Create grid
for i in range(width):
    for j in range(height):
        for k in range(num_tiles):
            grid[i,j,k] = model.NewBoolVar(f"[{i},{j}]:{k}")

# Exactly one true boolean per 2D grid space
for i in range(width):
    for j in range(height):
        num_tiles_in_spot = model.NewIntVar(0, num_tiles, f"num_tiles[{i}][{j}]")
        num_tiles_in_spot = sum([grid[i,j,k] for k in range(num_tiles)])
        model.Add(num_tiles_in_spot == 1)

# nl = []
# All adjacent tile constraints
for i in range(width):
    for j in range(height):
        for k in range(num_tiles):
            # For each adjacent position
            for index, (i2, j2) in enumerate([(i + 1, j), (i, j - 1), (i - 1, j), (i, j + 1)]):
                # If adjacent position is inside the grid
                if i2 >= 0 and i2 < width and j2 >= 0 and j2 < height:
                    model.AddBoolOr([grid[i2, j2, k2] for k2 in adjacency_mappings[k]["neighbors"][index]]).OnlyEnforceIf(grid[i, j, k])

# To break symmetry
model.Add(grid[3,3,10] == True)
# model.Add(grid[9,9,11] == True)

if solver.Solve(model) in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    # file = open("../Assets/Layouts/layout.txt", "w")
    for j in range(height):
        line = ""
        for i in range(width):
            for k in range(num_tiles):
                if solver.Value(grid[i,j,k]) == 1:
                    line += f"{k} "
        print(line)
        # file.write(line)
    # file.close()
else:
    print("Not Feasible")