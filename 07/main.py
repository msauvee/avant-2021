import game

def main(values):
    result = game.compute_puzzle1(values)
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2(values)
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    main(game.parse('data.txt'))