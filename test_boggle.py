import unittest
import boggle
from string import ascii_uppercase

class TestBoggle(unittest.TestCase):
    """
    Our test suite for boggle solver
    """
    
    def test_can_create_an_empty_grid(self):
        """
        Test to see if we can create an empty grid.
        Rather than assume a 3x3 grid we pass two arguments height and width or if you
        prefer row and column.The simplest grid is one with no rows or columns so 0 0 is used. 
        """
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)
        
    def test_grid_size_is_width_times_height(self):
        """
        Test is to ensure that the total size of the grid
        is equal to width * height
        """
        grid = boggle.make_grid(2,3)
        self.assertEqual(len(grid),6)
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all the coordinates 
        inside the grid can be accessed.
        We check if the position (0,0) can be found inside the grid.
        """
        grid = boggle.make_grid(2,2)
        self.assertIn((0,0),grid)
        self.assertIn((0,1),grid)
        self.assertIn((1,0),grid)
        self.assertIn((1,1),grid)
        self.assertNotIn((2,2),grid)
        
    
    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid
        contains letters
        """
        grid = boggle.make_grid(2,3)
        for letter in grid.values():
            self.assertIn(letter,ascii_uppercase)
        
    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours
        """
        coords = (1,2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0,1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
        
        
    def test_all_the_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2,2)
        neighbours = boggle.all_grid_neighbours(grid)
        self.assertEqual(len(neighbours), len(grid))
        for pos in grid:
            others = list (grid) # create a new list from the dictionary's keys
            # for each position the neighbors are the other three positions on the grid so we create the 
            #others list which is a full grid minus (-) the positioning question 
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
        
        
        
    