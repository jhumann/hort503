import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import random as random

class grid(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols))

    def print_grid(self):
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                state = self.grid[i][j]
                if state == 1:
                    print("X", end='')
                else:
                    print(" ", end='')
            print("\n", end='')

    def set_cell(self, x, y, state):
        self.grid[x][y] = state

    def next_move(self):
        curr_state = []
        for i in range(0, self.rows):
            col_list = []
            for j in range(0, self.cols):
                col_list.append(self.grid[i][j])
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
                    self.grid[i][j] = 0
                elif (num_neighbors == 2 or num_neighbors == 3) and me == 1:
                    self.grid[i][j] = 1
                elif num_neighbors > 3 and me == 1:
                    self.grid[i][j] = 0
                elif num_neighbors == 3 and me == 0:
                    self.grid[i][j] = 1


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

    def demo2(self, ticks = 100):
        for i in range(0, 1000):
            for x in range(1):
                x = random.randint(0,29)
            for y in range(1):
                y = random.randint(0,79)
            for z in range(1):
                z = random.randint(0,1)
            self.set_cell(x, y, z)
        self.play()

    def _animate(self, *args):
        # This is the callback function used by the
        # matlibplot.animation.FuncAnimation function.  It is responsible
        # for advanccing the game, and then setting the array for the image.
        # The requirements for the callback are that it must return a tuple
        # of 1 element containing the AxisImage object.
        if (self.rows <= 30 and self.cols <= 80):
            self.print_grid()
        self.next_move()
        self.im.set_array(self.grid)
        return (self.im,)


    def play(self):
        # Plays Conways' game of life and uses matplotlib to create an
        # animation of the changes in the grid.

        # First create a Figure object.  The Figure object contains all of
        # the plot elements.
        fig = plt.figure()

        # Create an AxisImage object using the imshow object. An AxisImage
        # object uses an array of points to represent pixels in an image.
        # Ee can use our numpy created grid to represent our pixels.  The colors
        # of the pixels are managed by the cmap argument.  Anything with a value
        # of zero is background and anything with a value of one is the
        # forground. Anything with a value between 0 and 1 is some gradient
        # value between the colors. In our case we only use 1 and zero..
        self.im = plt.imshow(self.grid, animated=True)

        # To get the image to be animated we have to create a FuncAnimation
        # object.  It receives as the Figure object, and the name of a function
        # that it will call each step of the animation.  The number of
        # miliseconds between each step of the animation is also given.
        anim = animation.FuncAnimation(fig, self._animate, interval=1)

        # Start the show!
        plt.show()
        #plt.savefig('test.png')

# this is just a test
def test_grid():
    temp_grid = grid(30,80)
    temp_grid.set_cell(29,79,1)
    temp_grid.print_grid()

# test_cell()
# test_grid()


gofl = grid(30, 80)
gofl.demo2()
