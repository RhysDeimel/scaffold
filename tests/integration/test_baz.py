import pytest

from scaffold import baz


@pytest.mark.incremental
class TestIncremental:
    def test_herp(self):
        assert baz.herp() != "Herp"

    def test_derp(self):
        assert baz.herp() == "Derp"
