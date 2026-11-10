import pytest
from scores import Scores

def test_empty_list():
    with pytest.raises(ValueError):
        Scores([])

def test_report_known_values():
    s = Scores([1, 2, 3])
    expected = "Mean: 2.00\nMedian: 2.00\nStd dev: 1.00"
    assert s.report() == expected

def test_values_unchanged():
    s = [1,2,3]
    sc = Scores(s)
    s.append(4)
    assert sc.mean() == 2

