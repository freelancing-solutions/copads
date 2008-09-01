import sys
import os
import unittest


o1 = 'the man is a dumb ass'.split(' ')
t1 = 'that man is a dumb ass'.split(' ')

class testD(unittest.TestCase):
    def testJaccard(self):
        self.assertEqual(D.Jaccard(o1, t1), 1.0-(5.0/7.0))
        
    def testNei_Li(self):
        self.assertEqual(D.Nei_Li(o1, t1), 1.0-(10.0/12.0))
        
    def testDice(self):
        self.assertEqual(D.Nei_Li(o1, t1), 5.0/(6.0 + 6.0))
        
    def testSokal_Michener(self):
        self.assertEqual(D.Sokal_Michener(o1, t1), 1.0-(5.0/7.0))
        
    def testHamming(self):
        self.assertEqual(D.Hamming(o1, t1), 1)
        
    def testKulczynski(self):
        pass
        
    def testLevenshtein(self):
        pass
        
    def testEuclidean(self):
        pass


if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(os.getcwd()), 'src'))
    import ObjectDistance as D
    unittest.main()