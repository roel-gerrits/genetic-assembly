
import unittest

from assembly.block import Block


class Test(unittest.TestCase):


    def testDepends(self):
        
        """
            2
        1 1 2
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 2, 0, 2, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        
        """
          2 2
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 1, 1, 2, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertTrue(b2.depends_on(b1))
        
        """
          2
          2
        1 1 1
        """
        b1 = Block(1, 0, 0, 2, 0)
        b2 = Block(2, 1, 1, 1, 2)
        self.assertFalse(b1.depends_on(b2))
        self.assertTrue(b2.depends_on(b1))
        
        """
        2 2 2
          1
        """
        b1 = Block(1, 1, 0, 1, 0)
        b2 = Block(2, 0, 1, 2, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertTrue(b2.depends_on(b1))
        
        """
        2 2
          1 1
        """
        b1 = Block(1, 1, 0, 2, 0)
        b2 = Block(2, 0, 1, 1, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertTrue(b2.depends_on(b1))
        
        """
        2 2
            1 1
        """
        b1 = Block(1, 2, 0, 3, 0)
        b2 = Block(2, 0, 1, 1, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        
        """
            2 2
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 2, 1, 3, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        
        """
            2
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 2, 1, 2, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        
        """
          2
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 1, 1, 1, 1)
        self.assertFalse(b1.depends_on(b2))
        self.assertTrue(b2.depends_on(b1))
        
        """
          2
          
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 1, 2, 1, 2)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        
        """
        2 2
          
        1 1
        """
        b1 = Block(1, 0, 0, 1, 0)
        b2 = Block(2, 0, 2, 1, 2)
        self.assertFalse(b1.depends_on(b2))
        self.assertFalse(b2.depends_on(b1))
        


if __name__ == "__main__":
    unittest.main()
