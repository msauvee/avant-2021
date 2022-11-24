def parse(filename):
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(line)
                
    return values

def compute_puzzle1(filename):
    values = parse(filename)
    count = 0
    for value in values:
        output_values = value.split(" | ")[1].strip().split()
        for output_value in output_values:
            if len(output_value) in (2, 3, 4, 7):
                count += 1
            
    return count

def crible(base, remove) -> str:
    for i in range(0, len(remove)):
        base = base.replace(remove[i], '')
    return base
    
def find_map_to_int(pattern_values):
    map_to_int = dict()
    map_to_segs = [0] * 10
    # numbers with unique number of segments
    for pattern_value in pattern_values:
        # number 1 : 2 segmets
        if len(pattern_value) == 2:
            map_to_int[pattern_value] = 1
            map_to_segs[1] = pattern_value
        # number 7 : 3 segmets
        elif len(pattern_value) == 3:
            map_to_int[pattern_value] = 7
            map_to_segs[7] = pattern_value
        # number 4 : 4 segmets
        elif len(pattern_value) == 4:
            map_to_int[pattern_value] = 4
            map_to_segs[4] = pattern_value
        # number 8 : 7 segmets
        elif len(pattern_value) == 7:
            map_to_int[pattern_value] = 8
            map_to_segs[8] = pattern_value
            
    for pattern_value in pattern_values:
        if len(pattern_value) == 5:
             # 2-7=3 and 2-4=3 
            if len(crible(pattern_value, map_to_segs[7])) == 3 and len(crible(pattern_value, map_to_segs[4])) == 3:
                map_to_int[pattern_value] = 2
                map_to_segs[2] = pattern_value   
            # 3-7=2 and 3-4=2
            elif len(crible(pattern_value, map_to_segs[7])) == 2 and  len(crible(pattern_value, map_to_segs[4])) == 2:
                map_to_int[pattern_value] = 3
                map_to_segs[3] = pattern_value     
            # 5-7=3 and  5-4=2       
            elif len(crible(pattern_value, map_to_segs[7])) == 3 and len(crible(pattern_value, map_to_segs[4])) == 2:
                map_to_int[pattern_value] = 5
                map_to_segs[5] = pattern_value     
        
        elif len(pattern_value) == 6:
            # 0-7 => 3 seg and 0-4=3
            if len(crible(pattern_value, map_to_segs[7])) == 3 and len(crible(pattern_value, map_to_segs[4])) == 3:
                map_to_int[pattern_value] = 0
                map_to_segs[0] = pattern_value   
            # 6-7 => 4 seg and 6-4=5
            elif len(crible(pattern_value, map_to_segs[7])) == 4 and len(crible(pattern_value, map_to_segs[4])) == 3:
                map_to_int[pattern_value] = 6
                map_to_segs[6] = pattern_value   
            # 9-7 => 3 seg and 9-4=2
            elif len(crible(pattern_value, map_to_segs[7])) == 3 and len(crible(pattern_value, map_to_segs[4])) == 2:
                map_to_int[pattern_value] = 9
                map_to_segs[9] = pattern_value   

    return map_to_int 
    
def compute_puzzle2(filename):
    values = parse(filename)
    sum = 0
    for value in values:
        pattern_values = value.split(" | ")[0].strip().split()
        output_values = value.split(" | ")[1].strip().split()
        n_pattern_values = [""] * 10
        n_output_values = [""] * 4
        for i in range(0, len(pattern_values)):
            n_pattern_values[i] = ''.join(sorted(pattern_values[i]))
        for i in range(0, len(output_values)):
            n_output_values[i] = ''.join(sorted(output_values[i]))
        map = find_map_to_int(n_pattern_values)
        value = map[n_output_values[0]]
        value = value*10 + map[n_output_values[1]]
        value = value*10 + map[n_output_values[2]]
        value = value*10 + map[n_output_values[3]]                
        sum += value     
               
    return sum
