def addition(a: float, b: float) -> float:
    if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
        raise TypeError("Inputs must be numeric")
    return a + b

print(addition(4.99, 90))