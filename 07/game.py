def parse(filename):
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                return list(map(int,line.split(',')))
                
    return None

def compute_puzzle(values, cost_func):
    max_pos = 0
    for value in values:
        max_pos = max(max_pos, value)
    fuel_consumptions = [0] * (max_pos+1)
    for pos in range(0, max_pos+1):
        fuel_consumptions[pos] = 0
        for value in values:
            fuel_consumptions[pos] += cost_func(value, pos)
    min_consumption = -1
    for i in range(len(fuel_consumptions)):
        if (min_consumption == -1 or min_consumption > fuel_consumptions[i]):
            min_consumption = fuel_consumptions[i]
    
    return min_consumption    
    
def cost_puzzle1(start, to):
    return abs(start-to)

def cost_puzzle2(start, to):
    n = abs(start-to)
    return int((n*(n+1))/2)

def compute_puzzle1(values):
    return compute_puzzle(values, cost_puzzle1)

def compute_puzzle2(values):
    return compute_puzzle(values, cost_puzzle2)