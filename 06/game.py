

def compute_puzzle1(values: list[int], days: int) -> int:
    counters = [0] * 9
    for value in values:
        counters[value] += 1
    for d in range(0, days):
        # new lanterns
        new = counters[0]
        for i in range(1, len(counters)):
            counters[i-1] = counters[i]
        counters[6] += new
        counters[8] = new    
        
    return sum(counters)    
