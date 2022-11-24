def compute_puzzle1(values) -> int:
    length = len(values[0])
    zero_count = [0] * length
    one_count = [0] * length
    for value in values:
        for i in range(0, length):
            if value[i] == '0':
                zero_count[i] += 1
            else:
                one_count[i] += 1
    
    gamma_rate = 0
    epsilon_rate = 0     
    for i in range(0, length):
        gamma_rate = gamma_rate * 2
        epsilon_rate = epsilon_rate * 2
        if (zero_count[i] > one_count[i]):
            epsilon_rate += 1
        else:
            gamma_rate += 1
            
    return gamma_rate * epsilon_rate

def crible(values, n, least):
    length = len(values[0])
    values_with_zero = []
    values_with_one = []
    zero_count = 0
    for value in values:
        if value[n] == '0':
            values_with_zero.append(value)
            zero_count += 1
        else:
            values_with_one.append(value)
    
    if least:
        new_values = values_with_zero if zero_count <= len(values) - zero_count else values_with_one
    else:
         new_values = values_with_zero if zero_count > len(values) - zero_count else values_with_one
    
    if len(new_values) == 1:
        return new_values[0]
    assert n < len(values[0])
    return crible(new_values, n+1, least)
    
def compute_puzzle2(values) -> int:
    rating_co2 = int(crible(values, 0, True), 2)
    rating_oxygen = int(crible(values, 0, False), 2)
    return rating_oxygen * rating_co2
