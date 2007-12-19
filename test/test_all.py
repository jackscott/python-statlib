import sys, unittest
from statlib import stats, pstat

try:
    from numpy import array as num_array
except ImportError:
    # numpy not installed
    sys.stderr.write('Numpy not installed ... skipping numpy tests\n')
    def num_array( values ):
        return values

class TestStatlib(unittest.TestCase):
    
    def setUp(self):
        "Gets called on each test"
        # generate list data
        self.L  = range( 1, 21 )
        self.LF = range( 1, 21 )
        self.LF[2] = 3.0
        self.LL = [ self.L ]*5

        # will test array data if numpy is installed
        self.A  = num_array( self.L )
        self.AF = num_array( self.LF )
        self.AA = num_array( self.LL )
        
        self.EQ = self.assertAlmostEqual

    def test_geometricmean(self):
        "Testing geometric mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for datum in data :
            self.EQ( stats.geometricmean( datum ), 8.304, 3)

    def test_harmonicmean(self):
        "Testing harmonic mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for datum in data :
            self.EQ( stats.harmonicmean( datum ), 5.559, 3)

    def test_mean(self):
        "Testing mean"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for datum in data :
            self.EQ( stats.mean( datum ), 10.5, 3)

    def test_median(self):
        "Testing median"
        data = [ self.L, self.LF, self.A, self.AF  ]
        for datum in data :
            self.assertTrue( 10 < stats.median( datum ) < 11 )

def get_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase( TestStatlib )
    return suite

if __name__ == '__main__':
    suite = get_suite()
    unittest.TextTestRunner(verbosity=2).run(suite)