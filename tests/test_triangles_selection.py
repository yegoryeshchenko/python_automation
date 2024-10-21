import pytest

from test_functions import triangle_area


class TestTrianglePositive:
    def test_triangle_1(self):
        assert round(triangle_area(1, 1, 1), 3) == 0.433

    @pytest.mark.positive
    @pytest.mark.my_positive
    @pytest.mark
    def test_triangle_1_2(self):
        assert round(triangle_area(1, 1, 1), 3) == 0


def test_triangle_2():
    assert round(triangle_area(2, 2, 2), 3) == 1.732
