import game

def main(filname):
    result = game.compute_puzzle1(filname)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(filname)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    # execute only if run as a script
    main('data.txt')