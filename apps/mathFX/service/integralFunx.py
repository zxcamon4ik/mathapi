import sympy as sp


def integral(const, func, n1, n2) -> dict:
    const_sym = sp.symbols(f"{const}")
    integral = sp.integrate(func, (const_sym, n1, n2))
    simplified_integral = sp.simplify(integral)
    steps = {
        "Integral": str(f"{integral} + C"),
    }
    return steps


def undefined_integral(const, func) -> dict:
    const_sym = sp.symbols(f"{const}")
    integral = sp.integrate(func, const_sym)
    simplified_integral = sp.simplify(integral)
    steps = {
        "Integral": str(f"{integral} + C"),
    }
    return steps
