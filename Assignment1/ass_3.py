

def arithmetic_operations(a, b):
    return {
        'addition': a + b,
        'subtraction': a - b,
        'multiplication': a * b,
        'division': a / b if b != 0 else 'undefined (division by zero)',
        'modulus': a % b if b != 0 else 'undefined (modulus by zero)',
        'exponentiation': a ** b,
        'floor_division': a // b if b != 0 else 'undefined (floor division by zero)'
    }


result = arithmetic_operations(10, 3)
for op, value in result.items():
    print(f"{op.capitalize()}: {value}")



