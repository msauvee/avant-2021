def parse(filename):
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(line.strip())
                
    return values

delimiters = [('(', ')', 3, 1), ('[', ']', 57, 2), ('{', '}', 1197, 3), ('<', '>', 25137, 4)]

def is_open(character):
    for delimiter in delimiters:
        if character == delimiter[0]:
            return True
    return False

def match(close, open):
    for delimiter in delimiters:
        if open == delimiter[0]:
            return close == delimiter[1]
    assert False    
    
def analyse_line(line):
    stack = []
    for i in range(0, len(line)):
        character = line[i]
        if is_open(character):
            stack.append(character)
        elif len(stack) == 0:
            return True, character, stack
        elif not match(character, stack[-1]):
            return True, character, stack
        else:
            stack.pop()
            
    return False, None, stack
    
def value_of(character):
    for delimiter in delimiters:
        if character == delimiter[1]:
            return delimiter[2]
    assert False    
    
def score_stack(stack):
    sum = 0
    stack.reverse()
    for character in stack:
        for delimiter in delimiters:
            if character == delimiter[0]:
                sum = sum * 5 + delimiter[3]
    return sum
        
def compute_puzzle1(filename):
    values = parse(filename)
    sum = 0
    for value in values:
        corrupted, illegal_character, _ = analyse_line(value)
        if corrupted:
            sum += value_of(illegal_character)
    return sum

def compute_puzzle2(filename):
    values = parse(filename)
    scores = []
    for value in values:
        corrupted, _, stack = analyse_line(value)
        if not corrupted:
            scores.append(score_stack(stack))
    scores.sort()
    return scores[int((len(scores)-1)/2)]