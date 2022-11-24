def compute(values) -> int:
    position = 0
    depth = 0
    for value in values:
        op = value.split()[0]
        count = int(value.split()[1])
        if op == 'forward':
            position += count
        elif op == 'down':
            depth += count
        else:
            depth -= count
    return position*depth

def compute2(values) -> int:
    position = 0
    depth = 0
    aim = 0
    for value in values:
        op = value.split()[0]
        count = int(value.split()[1])
        if op == 'forward':
            position += count
            depth += aim * count
        elif op == 'down':
            aim += count
        else:
            aim -= count
    return position*depth

def compute_puzzle1(values):
    return compute(values)

def compute_puzzle2(values):
    return  compute2(values)