import pytest

from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__d_less_than_zero():
    square_coefficient = 3.0
    linear_coefficient = -4.0
    const_coefficient = 2.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert (root_left, root_right) == (None, None)


def test__solve_square_equation__d_equals_zero():
    square_coefficient = 1.0
    linear_coefficient = -6.0
    const_coefficient = 9.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert (root_left, root_right) == (3.0, 3.0)


def test__solve_square_equation__d_more_than_zero():
    square_coefficient = 1.0
    linear_coefficient = -4.0
    const_coefficient = -5.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert (root_left, root_right) == (-1.0, 5.0)


def test__solve_square_equation__not_linear_and_square_coeffs():
    square_coefficient = 0.0
    linear_coefficient = 0.0
    const_coefficient = 2.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert (root_left, root_right) == (None, None)


def test__solve_square_equation__not_square_coefficient():
    square_coefficient = 0.0
    linear_coefficient = 1.0
    const_coefficient = 2.0

    root_left, root_right = solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)

    assert (root_left, root_right) == (-2.0, None)


def test_solve_square_equation__coefficients_not_float():
    square_coefficient = 'a'
    linear_coefficient = 'b'
    const_coefficient = 'c'

    with pytest.raises(TypeError):
        solve_square_equation(square_coefficient, linear_coefficient, const_coefficient)
