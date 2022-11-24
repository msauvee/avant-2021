import game
    
def main():
    result = game.compute_puzzle1('data.txt')
    print(f'Result to puzzle 1 is: {result}')
    result = game.compute_puzzle2('data.txt')
    print(f'Result to puzzle 2 is: {result}')

if __name__ == "__main__":
    main()