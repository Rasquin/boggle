from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    """
    Creates a grid (1st empty) that will hold all of the tiles
    for a boggle game
    """
    return{(row, col): choice(ascii_uppercase)
        for row in range(height)
        for col in range(width)}
    
    
def neighbours_of_position(coords):
    """
    Get neighbours of a given position
    """
    row = coords[0]
    col = coords[1]
    
    # Assign each of the neighbours
    # Top-left to top-right
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)

    # Left to right
    left = (row, col - 1)
    # The `(row, col)` coordinates passed to this function are situated here
    right = (row, col + 1)

    # Bottom-left to bottom-right
    bottom_left = (row + 1, col -1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)

    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]


def all_grid_neighbours(grid):
    """
    Get all of the possible neighbours for each position in
    the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    """
    Add all of the letters on the path to a string.
    Gets the list of letters for the positions in the path and then joins 
    them into a string
    """   
    return "".join([grid[p] for p in path])


""" 
Now we can erase this function, it was only to control the time

def word_in_dictionary(word, dict):
    return word in dict
"""
    
def search(grid, dictionary):
    """
    Search through the paths to locate words by matching strings to words in a dictionary
    """
    
    neighbours = all_grid_neighbours(grid)
    paths = []
    full_words, stems = dictionary #Now we have  failing the test_search_grid_for_words. Lets change the test to pass
    
    def do_search(path):  #para una sola posicion
        word = path_to_word(grid,path)
        if word in full_words :
            paths.append(path) #para palabras q se van formando con el mismo path
        if word not in stems:
            return
        for next_pos in neighbours[path[-1]]:#The last item in  the list path desde el cual comenzaras a buscar la siguiente letra
            if next_pos not in path: #para cortar la busqueda en ese path y cambiar d direccion
                do_search(path + [next_pos])
    
    for position in grid: #para cambiar de posicion
        do_search([position])
    
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)

    
def get_dictionary(dictionary_file):
    """
    Load dictionary file
    """
    
    """
    The right data structure. Our problem is that our word list is being stored in a
    Python list data structure which is O(n) lookup.
    Python has other data structures one of which is a set. Simply checking if an
    item exists in a set is on average O(1) operation this is even better than O
    (log n). It means that on average a set can say whether it contains a particular
    item or not in constant time. The time taken does not grow as a set grows.
    Converting our program to use a set instead of a list couldn't be simpler
    Find the get dictionary function change the square brackets on the last line to
    curly braces:

    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]
        
    with open(dictionary_file) as f:
        return {w.strip().upper() for w in f}
        
    If we knew at any point that no words in the dictionary start with the current path were constructing we
    would know that searching any further down that path is futile
    and we could abandon that path.
    """
  
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper() #capitalize words
            full_words.add(word)

            for i in range(1, len(word)):# get the stems
                stems.add(word[:i])

    return full_words, stems
        
def display_words(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))
    
    
# If you run this code now you will see that nothing happens.
#Our boggle solver is just a list of functions. If you run it nothing happens
#because there's no code to actually execute the functions. 

def main():
    """
    This is the function that will run the whole project.
    Let's just write a function that will generate a random board, load a
    dictionary, find the words and print them out. Place this function the bottom of
    the boggle py file
    """
    grid = make_grid(3,3)
    dictionary = get_dictionary('words.txt')
    words = search(grid,dictionary)
    display_words(words)
    
#main()

#Now that you've set up the boggle.py file to run there's a new problem when you run your
#unit tests You will find the program does more than just run the tests it
#runs the full solver. It creates a grid of letters, loads the dictionary
#and even prints a list of words. This is due to the way that importing files
#works in Python. When you import a file it gets executed. Your unit test file
#test_boggle.py imports boggle.py and then and in the process
#boggle.py gets executed this was fine when boggle.py only contained functions
#they got to find but only actually executed by the tests themselves. 
    
# The executing code should only be run when we actually run boggle.py from the command line
#it should be ignored if we're simply importing boggle.py into another file.
# To avoid running code when the file is imported we use the following 'if' statement 

if __name__ == "__main__":
    main()



    