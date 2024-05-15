import sympy as sp


def integral(const, func, n1, n2) -> dict:
    const_sym = sp.symbols(f"{const}")
    integral = sp.integrate(func, (const_sym, n1, n2))
    simplified_integral = sp.simplify(integral)
    steps = {
        "Step 1": "Compute integral of the function",
        "Integral": str(f"{integral} + C"),
        "Step 2": "Simplify the integral",
        "Simplified integral": str(f"{simplified_integral} + C")
    }
    return steps


def undefined_integral(const, func) -> dict:
    const_sym = sp.symbols(f"{const}")
    integral = sp.integrate(func, const_sym)
    simplified_integral = sp.simplify(integral)
    steps = {
        "Step 1": "Compute integral of the function",
        "Integral": str(f"{integral} + C"),
        "Step 2": "Simplify the integral",
        "Simplified integral": str(f"{simplified_integral} + C")
    }
    return steps
