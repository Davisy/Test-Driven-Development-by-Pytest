class TestInput:
    def test_a_input(self):
        a = 2

        assert type(a) != float
        assert a >= 0

    def test_b_input(self):
        b = 1.2

        assert type(b) != float
        assert b >= 0