import pytest

def increment(x):
    return x + 1

@pytest.mark.describe('#increment')
class TestIncrement:

        @pytest.mark.it('If given 0, should return 1')
        def test(self):
            """If given 0, should return 1"""
            assert increment(0) == 1