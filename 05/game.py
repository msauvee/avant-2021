class HydrotermalVent:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def parse(filename) -> tuple[list[HydrotermalVent], int, int]:
    vents = []
    x_max = 0
    y_max = 0
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                coordinates = line.strip().split(" -> ")
                x1 = int(coordinates[0].split(",")[0]) 
                y1 = int(coordinates[0].split(",")[1]) 
                x2 = int(coordinates[1].split(",")[0])
                y2 = int(coordinates[1].split(",")[1]) 
                vents.append(HydrotermalVent(x1, y1, x2, y2))
                x_max = max(x_max, x1, x2)
                y_max = max(y_max, y1, y2)
            
    return vents, x_max, y_max


def count_occurences(sea, n):
    count = 0
    for x in range(0, len(sea[0])):
        for y in range(0, len(sea)):
            if sea[y][x] >= n:
                count += 1
    return count
                
def compute_puzzle1(filename):
    vents, x_max, y_max = parse(filename)
    sea = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
    for vent in vents:
        if (vent.x1 == vent.x2):
            for y in range(min(vent.y1, vent.y2), max(vent.y1, vent.y2)+1):
                sea[y][vent.x1] = sea[y][vent.x1] + 1
        elif (vent.y1 == vent.y2):
            for x in range(min(vent.x1, vent.x2), max(vent.x1, vent.x2)+1):
                sea[vent.y1][x] = sea[vent.y1][x] + 1
        
    # check where there is 2
    return count_occurences(sea, 2)

def compute_puzzle2(filename):
    vents, x_max, y_max = parse(filename)
    sea = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
    for vent in vents:
        pos_x = vent.x1
        pos_y = vent.y1
        len_x = abs(vent.x1 - vent.x2)
        len_y = abs(vent.y1 - vent.y2)
        length = max(len_x, len_y)
        inc_x = 0 if len_x == 0 else int((vent.x2 - vent.x1)/len_x)
        inc_y = 0 if len_y == 0 else int((vent.y2 - vent.y1)/len_y)
        for c in range(0, length + 1):
            sea[pos_y][pos_x] = sea[pos_y][pos_x] + 1
            pos_x += inc_x
            pos_y += inc_y
        
    # check where there is 2
    return count_occurences(sea, 2)