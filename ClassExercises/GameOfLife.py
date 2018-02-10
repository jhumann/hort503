class cell(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state


class grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []

    def print_grid(self):
        self.grid = list()
        for x in range(self.rows):
            row_list = list()
            for y in range(self.cols):
                row_list.append(f"{y},{x}")
                #print(row_list)
            self.grid.append(row_list)
            print(self.grid)

    def next_move(self):
        pass

    def set_cell(self, x, y, state):
        pass

    def play(self, ticks):
        pass

test_cell = cell(15, 15, 1)
test_cell.get_state()
gofl = grid(30, 80)
gofl.set_cell(14, 40, 1)
gofl.set_cell(15, 42, 1)
gofl.set_cell(16, 39, 1)
gofl.set_cell(16, 40, 1)
gofl.set_cell(16, 43, 1)
gofl.set_cell(16, 44, 1)
gofl.set_cell(16, 35, 1)
gofl.print_grid()
