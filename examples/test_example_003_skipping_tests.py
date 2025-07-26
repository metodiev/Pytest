# examples/test_example_003_skipping_tests.py

import pytest
import sys

# Unconditionally skip this test with a reason
@pytest.mark.skip(reason="Not ready yet")
def test_unfinished_feature():
    assert 0  # This test will be skipped


# Conditionally skip if Python version < 3.8
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_python38_feature():
    # Some hypothetical code that requires Python 3.8+
    assert True


def test_normal():
    # This test runs normally
    assert 1 + 1 == 2
