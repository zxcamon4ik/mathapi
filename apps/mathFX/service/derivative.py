import sympy as sp


def take_derivative(const, func, sequence) -> dict:
    const_sym = f"{const}"
    derivative = func
    for _ in range(sequence):
        derivative = sp.diff(derivative, const_sym)
    simplified_derivative = sp.simplify(derivative)
    steps = {
        "derivative": str(f"{derivative}"),
    }
    return steps


