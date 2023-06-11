import pytest

from functions.level_1_5.two_square_equation import solve_square_equation


def test__solve_square_equation__three_coefficients():
    assert solve_square_equation(square_coefficient=1.0, 
                                 linear_coefficient=2.0, 
                                 const_coefficient=1.0) == (-1.0, -1.0)
    

def test__solve_square_equation__discriminant_less_zwro():
    assert solve_square_equation(square_coefficient=1.0, 
                                 linear_coefficient=1.0, 
                                 const_coefficient=1.0) == (None, None)
    

def test__solve_square_equation__not_square_coefficients():
    assert solve_square_equation(square_coefficient=0, 
                                 linear_coefficient=2.0, 
                                 const_coefficient=1.0) == (-0.5, None)
    

def test__solve_square_equation__only_const_coefficients():
    assert solve_square_equation(square_coefficient=0, 
                                 linear_coefficient=0, 
                                 const_coefficient=1.0) == (None, None)