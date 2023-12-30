'''
unittest / numpy.testing
'''

import unittest
from unittest import TestCase
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from graph_cellular_automata import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


M = np.array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0.],
       [0., 0., 0., 0., 0., 0., 1., 0., 1., 0., 0., 0.],
       [0., 0., 0., 0., 1., 1., 1., 0., 1., 1., 0., 1.],
       [0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [1., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 1., 1., 0., 0., 0., 0., 0., 1.],
       [0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 0., 0.],
       [0., 0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0.]])


states_in_M = np.array([[0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0]])
states_out_M = np.array([[0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1]])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class TestRunGCANeighborhood(TestCase):
    
    @staticmethod   
    def test_Run_GCA_in_neighborhood():
        np.testing.assert_array_equal(Run_GCA_in_neighborhood([M], th=0.35, output="binary"), states_in_M)
        
    @staticmethod   
    def test_Run_GCA_out_neighborhood():
        np.testing.assert_array_equal(Run_GCA_out_neighborhood([M], th=0.35, output="binary"), states_out_M)

        

if __name__ == '__main__':
    unittest.main()
    
    