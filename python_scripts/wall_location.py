import os 
from collections import defaultdict

def get_wall_location(): 
    file_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0] + "/Assets/Layouts/layout.txt"
    file = open(file_path, "r")

    lines = file.readlines()
    file.close()

    grid = {}

    # ignore the border tiles and set height and width 
    height = len(lines) - 2
    width = len(lines[0].split()) - 2

    for i in range(1, width + 1): 
        for j in range(1, height + 1): 
            grid[i, j] = defaultdict()
            grid[i, j]["wallTop"] = False
            grid[i, j]["wallRight"] = False
            grid[i, j]["wallBottom"] = False
            grid[i, j]["wallLeft"] = False

    for j in range(1, height + 1): 
        line = lines[j]
        chars = line.split()
        for i in range(1, width + 1): 
            char = chars[i]
            val = int(char)
            currPos = grid[i,j]
            if val == 4 or val == 16: 
                currPos["wallLeft"] = True
            if val == 5 or val == 17: 
                currPos["wallTop"] = True
            if val == 6 or val == 18: 
                currPos["wallRight"] = True
            if val == 7 or val == 19: 
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

    return grid, height, width
