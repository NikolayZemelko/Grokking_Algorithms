import pytest
from QuickSort.quicksort import qsort


@pytest.fixture
def array():
    return [5, 1, 23, 55, 6, 7, 62, 123, 23, 34, 4, 6, 7, 34, 7]

def test_quickSort(array):
    expected = sorted(array[:])
    array = qsort(array)
    assert array == expected
