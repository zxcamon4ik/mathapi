import sympy as sp


def integral(const, func, n1, n2):
    const_sym = sp.symbols(f"{const}")
    integral = sp.integrate(func, (const_sym, n1, n2))
    simplified_integral = sp.simplify(integral)
    return simplified_integral
