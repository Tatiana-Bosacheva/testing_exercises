import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize(
        "square_coefficient, linear_coefficient, const_coefficient, root_1, root_2", 
        [
            (3.0, -4.0, 2.0, None, None),
            (1.0, -6.0, 9.0, 3.0, 3.0),
            (1.0, -4.0, -5.0, -1.0, 5.0),
            (0.0, 0.0, 2.0, None, None),
            (0.0, 1.0, 2.0, -2.0, None),
        ]
)
def test_solve_square_equation(square_coefficient, linear_coefficient, const_coefficient, root_1, root_2):
    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
    assert (root_left, root_right) == (root_1, root_2)


def test_solve_square_equation__coefficients_not_float():
    square_coefficient = 'a'
    linear_coefficient = 'b'
    const_coefficient = 'c'

    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
