import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 4512

def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 1924

def test_compute_puzzle2_data():
    assert game.compute_puzzle2('data.txt') != 0
    
def test_gid():
    numbers = [49,48,98,84,71,59,37,36,6,21,46,30,5,33,3,62,63,45,43,35,65,77,57,75,19,44,4,76,88,92,12,27,7,51,14,72,96,9,0,17,83,64,38,95,54,20,1,74,69,80,81,56,10,68,42,15,99,53,93,94,47,13,29,34,60,41,82,90,25,85,78,91,32,70,58,28,61,24,55,87,39,11,79,50,22,8,89,26,16,2,73,23,18,66,52,31,86,97,67,40]
    grid = [[86, 46, 47, 61, 57], 
            [44, 74, 17, 5, 87], 
            [78, 8, 54, 55, 97], 
            [11, 90, 7, 75, 70], 
            [81, 50, 84, 10, 60]]
    board = game.Board(grid)
    boards = []
    boards.append(board)
    bingo = game.Bingo(numbers, boards)
    assert bingo.play2() != 0    