from hypothesis import given
from hypothesis.strategies import text, integers, from_regex, lists
import unittest
import doctest
import random
import sort

class TestSort(unittest.TestCase):
    def test_sort(self):
        data = [f'filename_{i}.py' for i in range(200)]
        temp = data[:]
        random.shuffle(temp)
        self.assertEqual(data, sort.sort(temp))


class TestSorting(unittest.TestCase):
    @given(from_regex(r'\A[a-z]*\Z'), integers(), lists(integers(min_value=0)))
    def test_sort(self, a, b, c):
        if len(a) == 0:
            i = 0
        else:
            i = b%(len(a)+1)

        strings = []

        for n in sorted(c):
            temp = list(a)
            temp.insert(i, str(n))
            strings.append(''.join(temp))
            print(strings[-1])

        print('\n\n\n')
        #self.assertEqual(decode(encode(s)), s)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == '__main__':
    unittest.main()
