def increment(x):
    return x + 1

class TestIncrement:

        def test_if_given_zero_should_return_one(self):
            """If given 0, should return 1"""
            assert increment(0) == 1