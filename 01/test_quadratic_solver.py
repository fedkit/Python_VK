from quadratic_solver import solve_quadratic_equation

assert solve_quadratic_equation(0, 0, 0) is None
assert solve_quadratic_equation(0, 0, -6) is None
assert solve_quadratic_equation(0, 10, -5) == tuple([0.5])
assert solve_quadratic_equation(0.23, 5, 101) is None
assert solve_quadratic_equation(1, 2, 1) == tuple([-1])
assert solve_quadratic_equation(5, 2, -7) == (-1.4, 1)
assert solve_quadratic_equation(1, 0, -4) == (-2, 2)