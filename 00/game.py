def parse(filename):
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(line)
                
    return values

def compute_puzzle1(values):
    return "Hello World!"

def compute_puzzle2(values):
    return "Hello World!"