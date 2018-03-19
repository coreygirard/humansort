from hypothesis import given
from hypothesis.strategies import text, integers, from_regex, lists, tuples
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



def gen_test_case(a, b, c):
    if len(a) == 0:
        i = 0
    else:
        i = b%(len(a)+1)

    strings = []
    for n in sorted(c):
        temp = list(a)
        temp.insert(i, str(n))
        strings.append(''.join(temp))

    return strings

def gen_test_data(data):
    temp = []
    data = sorted(data, key=lambda x: x[0])
    for a, b, c in data:
        temp.extend(gen_test_case(a, b, c))

    return temp

strat = from_regex(r'\A[a-z]+\Z'), integers(), lists(integers(min_value=0))
class TestSorting(unittest.TestCase):
    @given(lists(tuples(*strat)))
    def test_sort(self, e):
        strings = gen_test_data(e)
        backup = strings[:]
        random.shuffle(strings)

        self.assertEqual(backup, sort.sort(strings))


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == '__main__':
    unittest.main()
