import settings

CELL_SIZE = getattr(settings, 'cell_size', 10)


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cell(self):
        return (self.x/CELL_SIZE, self.y/CELL_SIZE)

    def adjacent_cells(self):
        cells = []
        cell = self.cell()
        for i in range(-1, 2):
            for j in range(-1, 2):
                cells.append((cell[0]+i, cell[1]+j))
        return cells

    def away_cells(self):
        cells = []
        cell = self.cell()
        for i in range(-2, 3):
            for j in range(-2, 3):
                cells.append((cell[0]+i, cell[1]+j))
        return cells

    def __unicode__(self):
        return '(%d, %d)' % (self.x, self.y)
