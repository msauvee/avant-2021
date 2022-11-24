import game

def main(filename):
    result = game.compute_puzzle1(filename)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(filename)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    main('data.txt')