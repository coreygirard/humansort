import doctest
import itertools
import random
import unittest

from hypothesis import given
from hypothesis.strategies import from_regex, integers, lists, tuples

from src.main import *


def test_sort():
    """Verifies simple ordering. IE '1' < '2' < '10' < '11' < '20' < '21'
    """
    data = ["filename_{}.py".format(i) for i in range(200)]
    temp = data[:]
    random.shuffle(temp)
    assert data == sort(temp)


def test_multi_template():
    """Ensures proper order is preserved with multiple formats
    """
    data = []
    data.extend(["{}_data.json".format(i) for i in range(50)])
    data.extend(["{}_log.csv".format(i) for i in range(50)])
    data.extend(["filename_{}.py".format(i) for i in range(50)])
    data.extend(["stuff_{}.py".format(i) for i in range(50)])
    temp = data[:]
    random.shuffle(temp)
    assert data == sort(temp)


def gen_index_via_mod(s, n):
    """Converts the provided integer 'n' into a valid insertion point
    in the string 's', ie the current index locations or at the end
    """
    if len(s) == 0:
        return 0

    return n % (len(s) + 1)


def remove_adjacent_nums(n):
    """Make sure we don't insert in adjacent locations, otherwise the numbers
    will join together and our created ordering will be invalid, failing test.
    """
    output = []
    for e in n:
        if len(output) == 0 or output[-1][0] <= e[0] - 2:
            output.append(e)
    return output


def split_to_indices_and_values(n):
    indices = []
    values = []

    for i, j in n:
        if j != []:
            indices.append(i)
            values.append(sorted(list(set(j))))
    return indices, values


def build_filename(s, indices, values):
    s = list(s)
    for (n, i), v in zip(enumerate(indices), values):
        s.insert(n + i, str(v))
    return "".join(s)


def gen_test_case(s, n):
    filenames = []

    n = [[gen_index_via_mod(s, i), j] for i, j in n]
    n = sorted(n, key=lambda x: x[0])
    n = remove_adjacent_nums(n)

    indices, values = split_to_indices_and_values(n)

    for v in itertools.product(*values):
        filenames.append(build_filename(s, indices, v))

    return filenames


def remove_duplicate_templates(data):
    # make sure that we don't have any duplicate templates
    tracker = set()
    output = []

    for e in data:
        if e[0] not in tracker:
            tracker.add(e[0])
            output.append(e)
    return output


def gen_test_data(data):
    filenames = []

    # remove duplicate templates (template meaning the string before any digits)
    data = remove_duplicate_templates(data)

    # sort the templates
    data = sorted(data, key=lambda x: x[0])

    for s, n in data:
        filenames.extend(gen_test_case(s, n))

    return filenames


# Create filename "templates", ie before digits
strat_strings = from_regex(r"\A[^0-9]*\Z")
strat_mod = tuples(integers(), lists(integers(min_value=0), max_size=10))

strat = strat_strings, lists(strat_mod, max_size=5)


@given(lists(tuples(*strat)))
def test_sort_property(e):
    strings = gen_test_data(e)
    backup = strings[:]
    random.shuffle(strings)
    assert backup == sort(strings)
