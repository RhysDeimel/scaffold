from scaffold import bar
import pytest


@pytest.mark.slow
def test_slowness():
    """To run this, use: pytest --runslow"""
    assert bar.slowbro() == "This is an intentionally slow test"
