class Octopuse:
    flash_count = 0
    def __init__(self, level):
        self.level = level
        self.neighbours = []
        self.has_flashed = False
        self.flash_count = 0
        
    def inc(self):
        self.level += 1
        self.has_flashed = False
        
    def flash(self):
        if self.has_flashed: 
            return
        self.level += 1
        self.check_flash()
        
    def check_flash(self):
        if self.has_flashed:
            return
        if self.level < 10:
            return
        self.level = 0
        self.has_flashed = True
        self.flash_count += 1
        for neigthbour in self.neighbours:
            neigthbour.flash()

class Grid:
    
    def __init__(self, values):
        self._octopuses = []
        for value in values:
            octopuses = []
            for character in value:
                octopuses.append(Octopuse(int(character)))
            self._octopuses.append(octopuses)
            
        for y in range(0, len(self._octopuses)):
            for x in range(0, len(self._octopuses[y])):
                neigthbours = []
                self._append_negthbour(x-1, y-1, neigthbours)
                self._append_negthbour(x-1, y, neigthbours)
                self._append_negthbour(x-1, y+1, neigthbours)
                self._append_negthbour(x, y-1, neigthbours)
                self._append_negthbour(x, y+1, neigthbours)
                self._append_negthbour(x+1, y-1, neigthbours)
                self._append_negthbour(x+1, y, neigthbours)
                self._append_negthbour(x+1, y+1, neigthbours)
                    
                self._octopuses[y][x].neighbours = neigthbours

    def _append_negthbour(self, x, y, neigthbours):
        if y >=0 and y < len(self._octopuses) and x >= 0 and x < len(self._octopuses[y]):
            neigthbours.append(self._octopuses[y][x])
        
    def write(self):
        values = []
        for y in range(0, len(self._octopuses)):
            value = ""
            for x in range(0, len(self._octopuses[y])):
                value += str(self._octopuses[y][x].level) if self._octopuses[y][x].level < 10 else '+'
            values.append(value)
        return values
        
    def do_step(self):
        for y in range(0, len(self._octopuses)):
            for x in range(0, len(self._octopuses[y])):
                self._octopuses[y][x].inc()
        for y in range(0, len(self._octopuses)):
            for x in range(0, len(self._octopuses[y])):
                self._octopuses[y][x].check_flash()   
                
    def flash_count(self):
        count = 0
        for y in range(0, len(self._octopuses)):
            for x in range(0, len(self._octopuses[y])):
                count += self._octopuses[y][x].flash_count
        return count

    def all_octop_flashed(self):
        for y in range(0, len(self._octopuses)):
            for x in range(0, len(self._octopuses[y])):
                if not self._octopuses[y][x].has_flashed:
                    return False
        return True

def parse(filename):
    values = []
    with open(filename) as f:
        for line in f:
            if line[-1:] == '\n':
                line = line[:-1]
            if len(line) > 0:
                values.append(line.strip())
                
    return values

def compute_puzzle1(filename):
    grid = Grid(parse(filename))
    for i in range(0,100):
        grid.do_step()
        
    return grid.flash_count()

def compute_puzzle2(filename):
    grid = Grid(parse(filename))
    count = 0
    while (not grid.all_octop_flashed()):
        count += 1
        grid.do_step()
        
    return count