from ortools.sat.python import cp_model

# from .tile_rules import tile_rules

model = cp_model.CpModel()
solver = cp_model.CpSolver()

width = 5
height = 5
num_tiles = 3
grid = {}

tile_rules = {
    0: {
        "posX": [],
        "negX": [],
        "posZ": [],
        "negZ": [],
    },
    1: {
        "posX": [],
        "negX": [],
        "posZ": [],
        "negZ": [],
    },
    2: {
        "posX": [],
        "negX": [],
        "posZ": [],
        "negZ": [],
    },
    3: {
        "posX": [],
        "negX": [],
        "posZ": [],
        "negZ": [],
    },
}

# Create grid
for i in range(width):
    for j in range(height):
        for k in range(num_tiles):
            grid[i,j,k] = model.NewBoolVar(f"[{i},{j}]:{k}")

# Exactly one true boolean per grid space
for i in range(width):
    for j in range(height):
        num_tiles_in_spot = model.NewIntVar(0, num_tiles, f"num_tiles[{i}][{j}]")
        num_tiles_in_spot = sum([grid[i,j,k] for k in range(num_tiles)])
        model.Add(num_tiles_in_spot == 1)

if solver.Solve(model) in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    # for i in range(width):
    #     for j in range(height):
    #         for k in range(num_tiles):
    #             if solver.Value(grid[i,j,k]) == 1:
    #                 print(f"[{i},{j}]:{k}")
    [print(f"[{i},{j}]:{k}") for i in range(width) for j in range(height) for k in range(num_tiles) if solver.Value(grid[i,j,k]) == 1]
else:
    print("Not feasible")