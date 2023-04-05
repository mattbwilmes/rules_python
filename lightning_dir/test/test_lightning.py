import sys
import pytest

import lightning

def test_assert():
  assert True

if __name__ == "__main__":
  sys.exit(pytest.main([__file__]))
