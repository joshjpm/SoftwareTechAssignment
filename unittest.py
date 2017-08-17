import unittest
from word_ladder import find, same, build
from word_ladder import *


class sameTest1(unittest.TestCase):
    def test_same1(self):
        self.assertEqual(same('lead', 'gold'), 1)
class sameTest2(unittest.TestCase):
    def test_same2(self):
        self.assertEqual(same('goad', 'gold'), 3)
class sameTest3(unittest.TestCase):
    def test_same3(self):
        self.assertEqual(same('gold', 'gold'), 4)
class sameTest4(unittest.TestCase):
    def test_same4(self):
        self.assertEqual(same('frank', 'gold'), 0)

class findTest1(unittest.TestCase):
    def test_find1(self):
        self.assertEqual(find('load', words, seen, 'gold', ['lead', 'load']), True)
class findTest2(unittest.TestCase):
    def test_find2(self):
        self.assertIsNone(find('photo', words, seen, 'hosue', ['photo']))
class findTest3(unittest.TestCase):
    def test_find3(self):
        self.assertEqual(find('gold', words, seen, 'gold', ['goad', 'load']), True)


class buildTest1(unittest.TestCase):
    def test_build1(self):
        self.assertEqual(build('.ead', words, seen, ['bead', 'dead', 'head', 'mead', 'read']), word)


if __name__ == '__main__':
    unittest.main(exit=False)
