import sympy as sp


def take_derivative(const, func, sequence) -> dict:
    const_sym = f"{const}"
    derivative = func
    for _ in range(sequence):
        derivative = sp.diff(derivative,const_sym)
    simplified_derivative = sp.simplify(derivative)
    steps = {
        "Step 1": "Compute integral of the function",
        "Integral": str(f"{derivative} + C"),
        "Step 2": "Simplify the integral",
        "Simplified integral": str(f"{simplified_derivative} + C")
    }
    return steps


