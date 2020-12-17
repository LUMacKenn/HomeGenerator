from ortools.sat.python import cp_model
from collections import defaultdict
import os 

model = cp_model.CpModel()
solver = cp_model.CpSolver()

grid = {}

# width = 10
# height = 10
max_lamps = 15

# note where the walls are 
file = open("../HomeGenerator/Assets/Layouts/layout.txt", "r")

lines = file.readlines()

# ignore the border tiles and set height and width 
height = len(lines) - 2
width = len(lines[0].split()) - 2

# include border tile grid spots (for debugging purposes)
for i in range(1, width + 1): 
    for j in range(1, height + 1): 
        grid[i, j] = defaultdict()
        grid[i, j]["wallTop"] = False
        grid[i, j]["wallRight"] = False
        grid[i, j]["wallBottom"] = False
        grid[i, j]["wallLeft"] = False

# # walls on the edges
# for i in range(width): 
#     grid[1, i]["wallTop"] = True
#     grid[height - 2, i]["wallBottom"] = True
#     grid[i, 1]["wallLeft"] = True
#     grid[i, width - 2]["wallRight"] = True

for i in range(1, height + 1): 
    line = lines[i]
    chars = line.split()
    for j in range(1, width + 1): 
        char = chars[j]
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
for i in range(1, width + 1): 
    for j in range(1, height + 1): 
        hasLamp[i, j] = model.NewBoolVar("hasLamp[%s, %s]" % (i, j))

SAME_TILE_SCORE = 40
RADIUS_ONE_SCORE = 30
RADIUS_TWO_SCORE = 20

total_score = model.NewIntVar(0, 10000, "total_light_scores")
# total_score = 0
# total_scores = []

def addScore(posX, posY, scores, score): 
    lightscore = model.NewIntVar(0, 100, "light score of grid [%s, %s]" % (posX, posY))
    model.Add(lightscore == score).OnlyEnforceIf(hasLamp[posX, posY])
    model.Add(lightscore == 0).OnlyEnforceIf(hasLamp[posX, posY].Not())
    scores.append(lightscore)

for i in range(1, width + 1): 
    for j in range(1, height + 1): 
        scores = []
        currPos = grid[i, j]
        # check if lamp in curr grid pos
        addScore(i, j, scores, SAME_TILE_SCORE)

        # check first radius and second radius (direct)
        if currPos["wallTop"] is False: 
            addScore(i - 1, j, scores, RADIUS_ONE_SCORE)
            nextPos = grid[i - 1, j]

            if nextPos["wallTop"] is False: 
                addScore(i - 2, j, scores, RADIUS_TWO_SCORE)

        if currPos["wallRight"] is False: 
            addScore(i, j + 1, scores, RADIUS_ONE_SCORE)
            nextPos = grid[i, j + 1]

            if nextPos["wallRight"] is False: 
                addScore(i, j + 2, scores, RADIUS_TWO_SCORE)

        if currPos["wallBottom"] is False: 
            addScore(i + 1, j, scores, RADIUS_ONE_SCORE)
            nextPos = grid[i + 1, j]

            if nextPos["wallBottom"] is False: 
                addScore(i + 2, j, scores, RADIUS_TWO_SCORE)

        if currPos["wallLeft"] is False: 
            addScore(i, j - 1, scores, RADIUS_ONE_SCORE)

            nextPos = grid[i, j - 1]
            if nextPos["wallLeft"] is False: 

                addScore(i, j - 2, scores, RADIUS_TWO_SCORE)

        if currPos["wallTop"] is False and currPos["wallRight"] is False: 
            addScore(i - 1, j + 1, scores, RADIUS_TWO_SCORE)

        if currPos["wallTop"] is False and currPos["wallLeft"] is False: 
            addScore(i - 1, j - 1, scores, RADIUS_TWO_SCORE)

        if currPos["wallBottom"] is False and currPos["wallRight"] is False: 
            addScore(i + 1, j + 1, scores, RADIUS_TWO_SCORE)
        
        if currPos["wallBottom"] is False and currPos["wallLeft"] is False: 
            addScore(i + 1, j - 1, scores, RADIUS_TWO_SCORE)

        sum_scores = model.NewIntVar(0, 50, "sum_scores for grid[%s, %s]" % (i, j))
        model.Add(sum_scores == sum(scores))
        total_score += sum_scores

sum_lamps = model.NewIntVar(0, width*height, "sum_lamps")
model.Add(sum_lamps == sum(hasLamp[i, j] for i in range(1, width + 1) for j in range(1, height + 1)))
model.Add(sum_lamps == max_lamps)
model.Maximize(total_score)
        
if solver.Solve(model) in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    file_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0] + "/Assets/Layouts/lampLayout.txt"
    print(solver.Value(total_score))
    file = open(file_path, "w")


    # add 2 to widths and heights to account again for border tiles
    first_last_row = ""
    for i in range(width + 2): 
        first_last_row += "0 "
    first_last_row += "\n"
    file.write(first_last_row)
    
    # set first and last width vals as 0 - border tiles
    for i in range(1, width + 1): 
        line = "0 "
        for j in range(1, height + 1): 
            if solver.Value(hasLamp[i, j]) == 1: 
                line += "1 "
            else: 
                line += "0 "
            if j == height: 
                line += "0 \n"
        # print(line)
        file.write(line)
    file.write(first_last_row)
    print("New Lights Layout Created!")
    print(solver.ResponseStats())
else:
    print("Not Feasible")



