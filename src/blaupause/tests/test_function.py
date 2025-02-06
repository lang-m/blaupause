from blaupause import add
import pytest


def test_add():
    assert add(0, 0) == 0
    assert add(1, 2) == 3
    assert add(0, -1.2) == -1.2
    with pytest.raises(TypeError):
        assert add('x', 2)
