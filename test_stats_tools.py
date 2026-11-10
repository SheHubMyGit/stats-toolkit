import pytest
from stats_tools import mean, median, std_dev, to_number, is_valid_score

def test_mean_basic():
    assert mean([1, 2, 3, 4]) == 2.5

def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])

def test_std_dev_known_value():
    assert std_dev([2, 4, 6]) == pytest.approx(2.0)

def test_median_odd_even():
  assert median([1,2,3,4,5]) == 3

def test_median_even():
  assert median([1,2,3,4,5,6]) == 3.5

def test_median_empty():
  with pytest.raises(ValueError):
    median([])

def test_std_dev_no_spread():
  with pytest.raises(ValueError):
    std_dev([])
  with pytest.raises(ValueError):
    std_dev([5])

def test_to_number_works():
  assert to_number("72") == 72.0
  assert to_number("7o") is None
  assert to_number("") is None

def test_is_valid_score_works():
  assert is_valid_score(-1) == False
  assert is_valid_score(100.5) == False
  assert is_valid_score(100) == True
  assert is_valid_score(0) == True

def test_median_unchanged():
  m = [3,1,5,6,4,2]
  snap = m.copy()
  median(m)
  assert snap == m
