class cell(object):
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

# this is just a test
def test_cell():
    temp_cell = cell(4,5,1)
    print(temp_cell.get_state())
    temp_cell.set_state(0)
    print(temp_cell.get_state())


class grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = []
        for i in range(0, rows):
            col_list = []
            for j in range(0, cols):
                col_list.append(cell(i, j, 0))
            self.grid.append(col_list)

    def print_grid(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                state = self.grid[i][j].get_state()
                if state == 1:
                    print("X", end='')
                else:
                    print(" ", end='')
            print("\n", end='')


    def set_cell(self, x, y, state):
        self.grid[x][y].set_state(state)

    def next_move(self):
        curr_state = []
        for i in range(0, self.rows):
            col_list = []
            for j in range(0, self.cols):
                col_list.append(self.grid[i][j].get_state())
            curr_state.append(col_list)

        for i in range(1, self.rows - 1):
            for j in range(1, self.cols - 1):
                nw = curr_state[i-1][j-1]
                n = curr_state[i-1][j]
                ne = curr_state[i-1][j+1]
                w = curr_state[i][j-1]
                me = curr_state[i][j]
                e = curr_state[i][j+1]
                sw = curr_state[i+1][j-1]
                s = curr_state[i+1][j]
                se = curr_state[i+1][j+1]

                num_neighbors = ne + n + nw + e + w + se + s + sw

                if num_neighbors < 2 and me == 1:
                    self.grid[i][j].set_state(0)
                elif (num_neighbors == 2 or num_neighbors == 3) and me == 1:
                    self.grid[i][j].set_state(1)
                elif num_neighbors > 3 and me == 1:
                    self.grid[i][j].set_state(0)
                elif num_neighbors == 3 and me == 0:
                    self.grid[i][j].set_state(1)


    def play(self, ticks = 100):
        for i in range(0, ticks):
            print(f"Step {i+1}")
            self.next_move()
            self.print_grid()

    def demo1(self, ticks = 100):
        self.set_cell(14, 40, 1)
        self.set_cell(15, 42, 1)
        self.set_cell(16, 39, 1)
        self.set_cell(16, 40, 1)
        self.set_cell(16, 43, 1)
        self.set_cell(16, 44, 1)
        self.set_cell(16, 45, 1)
        self.play(ticks)

# this is just a test
def test_grid():
    temp_grid = grid(30,80)
    temp_grid.set_cell(29,79,1)
    temp_grid.print_grid()

# test_cell()
# test_grid()


gofl = grid(30, 80)
gofl.demo1()
