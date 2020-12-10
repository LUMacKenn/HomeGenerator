from ortools.sat.python import cp_model
from collections import defaultdict

model = cp_model.CpModel()
solver = cp_model.CpSolver()

grid = {}

width = 10
height = 10
max_lamps = 5

for i in range(width): 
    for j in range(height): 
        grid[i, j] = defaultdict()
        grid[i, j]["wallTop"] = False
        grid[i, j]["wallRight"] = False
        grid[i, j]["wallBottom"] = False
        grid[i, j]["wallLeft"] = False

# walls on the edges
for i in range(width): 
    grid[0, i]["wallTop"] = True
    grid[height - 1, i]["wallBottom"] = True
    grid[i, 0]["wallLeft"] = True
    grid[i, width - 1]["wallRight"] = True

# note where the walls are 
file = open("../HomeGenerator/Assets/Layouts/layout2.txt", "r")

lines = file.readlines()
for i, line in enumerate(lines): 
    chars = line.split()
    for j, char in enumerate(chars): 
        # print(char)
        val = int(char)
        currPos = grid[i,j]
        if val == 4: 
            currPos["wallLeft"] = True
        if val == 5: 
            currPos["wallTop"] = True
        if val == 6: 
            currPos["wallRight"] = True
        if val == 7: 
            currPos["wallBottom"] = True
        if val == 8: 
            currPos["wallLeft"] = True
            currPos["wallTop"] = True
        if val == 9: 
            currPos["wallRight"] = True
            currPos["wallTop"] = True
        if val == 10: 
            currPos["wallRight"] = True
            currPos["wallBottom"] = True
        if val == 11: 
            currPos["wallLeft"] = True
            currPos["wallBottom"] = True

hasLamp = {}
lightScore = {}
for i in range(width): 
    for j in range(height): 
        hasLamp[i, j] = model.NewBoolVar("hasLamp[%s, %s]" % (i, j))
        # lightScore[i, j] = model.NewBoolVar("lightScore[%s, %s]" % (i, j))

SAME_TILE_SCORE = 50
RADIUS_ONE_SCORE = 20
RADIUS_TWO_SCORE = 10

total_score = model.NewIntVar(0, 10000, "total_light_scores")
# total_score = 0
# total_scores = []

for i in range(width): 
    for j in range(height): 
        scores = []
        currPos = grid[i, j]
        # check if lamp in curr grid pos
        same_place_score = model.NewIntVar(0, 100, "light score of grid %s, %s]" % (i, j))
        model.Add(same_place_score == SAME_TILE_SCORE).OnlyEnforceIf(hasLamp[i, j])
        model.Add(same_place_score == 0).OnlyEnforceIf(hasLamp[i, j].Not())
        scores.append(same_place_score)

        # model.Add(hasLamp)
        # check first radius 
        if currPos["wallTop"] is False: 
            # print("%s, %s,: reached" % (i, j))
            # score = model.NewIntVar(0, RADIUS_ONE_SCORE, f"light score of top of grid[{i}, {j}]")
            score = model.NewIntVar(0, 100, "light score of top of grid %s, %s]" % (i, j))
            model.Add(score == RADIUS_ONE_SCORE).OnlyEnforceIf(hasLamp[i - 1, j])
            model.Add(score == 0).OnlyEnforceIf(hasLamp[i - 1, j].Not())
            scores.append(score)
        if currPos["wallRight"] is False: 
            # score = model.NewIntVar(0, RADIUS_ONE_SCORE, f"light score of right of grid[{i}, {j}]")
            score = model.NewIntVar(0, 100, "light score of right of grid[%s, %s]" % (i, j))
            model.Add(score == RADIUS_ONE_SCORE).OnlyEnforceIf(hasLamp[i, j + 1])
            model.Add(score == 0).OnlyEnforceIf(hasLamp[i, j + 1].Not())
            scores.append(score)
        if currPos["wallBottom"] is False: 
            # score = model.NewIntVar(0, RADIUS_ONE_SCORE, f"light score of bottom of grid[{i}, {j}]")
            score = model.NewIntVar(0, 100, "light score of bottom of grid[%s, %s]" %(i, j))
            model.Add(score == RADIUS_ONE_SCORE).OnlyEnforceIf(hasLamp[i + 1, j])
            model.Add(score == 0).OnlyEnforceIf(hasLamp[i + 1, j].Not())
            scores.append(score)
        if currPos["wallLeft"] is False: 
            #score = model.NewIntVar(0, RADIUS_ONE_SCORE, f"light score of left of grid[{i}, {j}]")
            score = model.NewIntVar(0, 100, "light score of left of grid[%s, %s]" % (i, j))
            model.Add(score == RADIUS_ONE_SCORE).OnlyEnforceIf(hasLamp[i, j - 1])
            model.Add(score == 0).OnlyEnforceIf(hasLamp[i, j - 1].Not())
            scores.append(score)

        total_score += sum(scores)

sum_lamps = model.NewIntVar(0, width*height, "sum_lamps")
model.Add(sum_lamps == sum(hasLamp[i, j] for i in range(width) for j in range(height)))
model.Add(sum_lamps == max_lamps)
model.Maximize(total_score)
        
if solver.Solve(model) in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    # print(solver.Value(lightScore[1,1]))
    #file = open("../Assets/Layouts/layout.txt", "w")
    for i in range(width): 
        line = ""
        for j in range(height): 
            if solver.Value(hasLamp[i, j]) == 1: 
                line += "1 "
            else: 
                line += "0 "
        print(line)
    print(solver.ResponseStats())
else:
    print("Not Feasible")



