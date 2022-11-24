def parse(filename):
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(list(map(lambda x: int(x),line)))
                
    return values

def compute_puzzle1(filename):
    values = parse(filename)
    risk = 0
    for y in range(0, len(values)):
        for x in range(0, len(values[y])):
            adjacents=[]
            if y>0:
                adjacents.append(values[y-1][x])
            if y+1<len(values):
                adjacents.append(values[y+1][x])
            if x>0:
                adjacents.append(values[y][x-1])
            if x+1<len(values[y]):
                adjacents.append(values[y][x+1])
            if values[y][x] < min(adjacents):
                risk += values[y][x]+1
    
    return risk

def find_low_points(values):
    low_points = []
    for y in range(0, len(values)):
        for x in range(0, len(values[y])):
            adjacents=[]
            if y>0:
                adjacents.append(values[y-1][x])
            if y+1<len(values):
                adjacents.append(values[y+1][x])
            if x>0:
                adjacents.append(values[y][x-1])
            if x+1<len(values[y]):
                adjacents.append(values[y][x+1])
            if values[y][x] < min(adjacents):
                low_points.append((x,y))
    
    return low_points

def check_adjacent(values, value, x, y, points, flood_points, new_flood):
    if y<0 or y>=len(values) or x<0 or x>=len(values[y]):
        return
    if values[y][x] == 9:
        return
    # already found
    if (x,y) in flood_points:
        return
    # will be processed later
    if (x,y) in new_flood:
        return 
    if values[y][x] > value:
        points.append((x, y))

def adjacent_floods(values, flood_point, flood_points, new_flood):
    points = []
    x = flood_point[0]
    y = flood_point[1]
    value = values[y][x]
    check_adjacent(values, value, x, y-1, points, flood_points, new_flood)
    check_adjacent(values, value, x, y+1, points, flood_points, new_flood)
    check_adjacent(values, value, x-1, y, points, flood_points, new_flood)
    check_adjacent(values, value, x+1, y, points, flood_points, new_flood)
    return points
                
def compute_size(values, x, y) -> int:
    new_flood = [(x, y)]
    flood_points = []
    while (len(new_flood) > 0):
        flood_point = new_flood.pop()
        flood_points.append(flood_point)
        new_flood.extend(adjacent_floods(values, flood_point, flood_points, new_flood))
    
    return len(flood_points)  
    
    
def compute_puzzle2(filename):
    values = parse(filename)
    low_points = find_low_points(values)
    size = []
    for low_point in low_points:
        size.append(compute_size(values, low_point[0], low_point[1]))
        
    size.sort(reverse=True)
    return size[0]*size[1]*size[2]

