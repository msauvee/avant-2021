import game

    
def test_compute_puzzle1_80():
    assert game.compute_puzzle1([3,4,3,1,2], 80) == 5934
    
    
def test_compute_puzzle1_18():
    assert game.compute_puzzle1([3,4,3,1,2], 18) == 26

def test_compute_puzzle1_256():
    assert game.compute_puzzle1([3,4,3,1,2], 256) == 26984457539 



    