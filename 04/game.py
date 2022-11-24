from typing import List


class Board:
    counter=0
    def __init__(self, grid):
        self._counter = Board.counter
        Board.counter += 1
        self._grid = grid
        self.closed = False
        self._numbers = []

    def _does_win(self) -> bool:
        length = len(self._grid[0]);
        for i in range(length):
            count_row = 0
            count_column = 0
            for j in range(length):
                # check rows
                if self._grid[i][j] in self._numbers:
                    count_row += 1
                # check coluns
                if self._grid[j][i] in self._numbers:
                    count_column += 1
            if count_row == length or count_column == length:
                return True
        return False
        
    def _sum_unmark(self) -> int:
        sum = 0
        for row in self._grid:
            for value in row:
                if not (value in self._numbers):
                    sum += value
        return sum 
        
    def add(self, number: int) -> int:
        self._numbers.append(number)
        if self._does_win():
            self.closed = True
            return number * self._sum_unmark()
        return 0

class Bingo:
    def __init__(self, numbers: list[int], boards: list[Board]):
        self._numbers = numbers
        self._boards = boards

    def play1(self) -> int:
        for number in self._numbers:
            for board in self._boards:
                win = board.add(number)
                if win > 0:
                    return win

        return 0
    
    def play2(self) -> int:
        for number in self._numbers:
            board_processed_count = 0
            for board in self._boards:
                if board.closed:
                    continue
                board_processed_count += 1
                win = board.add(number)
            if win != 0 and board_processed_count == 1:
                return win

        assert False, "should not occur"


def _read_numbers(line: str) -> list[int]:
    return list(map(int, line.strip().split(',')))


def _read_grid(line: str) -> list[int]:
    return list(map(int, line.strip().split()))


def parse(filename) -> Bingo:
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(line)

    numbers = _read_numbers(values[0])
    boards = []
    for i in range(0, int((len(values)-1)/5)):
        grid = []
        grid.append(_read_grid(values[1+i*5]))
        grid.append(_read_grid(values[2+i*5]))
        grid.append(_read_grid(values[3+i*5]))
        grid.append(_read_grid(values[4+i*5]))
        grid.append(_read_grid(values[5+i*5]))
        boards.append(Board(grid))
    return Bingo(numbers, boards)


def compute_puzzle1(filename) -> int:
    bingo = parse(filename)
    return bingo.play1()

def compute_puzzle2(filename) -> int:
    bingo = parse(filename)
    return bingo.play2()
