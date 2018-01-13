import unittest
import line

class LineTests(unittest.TestCase):
   def test_line(self):
     testline = line.Line(1, 1, 3, 7)
        self.assertEqual(testline.x1, 1)

      # Add code here.
      # 1) Create a Line with x1, y1, x2, y2 values of your choice.
      # 2) Use assertEqual on each field in the new Line to verify
      #    that it holds the expected value.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

