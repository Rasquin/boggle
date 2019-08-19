




# Example of how we use unittest

import unittest

class test_boggle(unittest.TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(1,1)

# Meaning of ---> if __name__ == "__main__":

Every module in python has a special attribute called __name__ . 
The value of __name__  attribute is set to '__main__'  when module run as main program. 
Otherwise the value of __name__  is set to contain the name of the module.