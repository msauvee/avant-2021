import game

def test_compute_puzzle1():
    assert game.compute_puzzle1('example.txt') == 26

def test_compute_puzzle2_simple():
    assert game.compute_puzzle2('example2.txt') == 5353
   
def test_compute_puzzle2():
    assert game.compute_puzzle2('example.txt') == 61229 
    



    