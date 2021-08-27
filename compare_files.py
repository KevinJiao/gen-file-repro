import unittest

class TestCompareFiles(unittest.TestCase):
  def test_compare_files(self):
    ref = open('ref.txt').read()
    test = open('test.txt').read()
    self.assertTrue(len(ref) != 0)
    self.assertTrue(len(test) != 0)

    self.assertEqual(ref, test)

if __name__ == '__main__':
  unittest.main()
