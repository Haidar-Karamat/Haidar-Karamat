def cal_sum_prod(x: int, y: int, z:int) -> int:
    return x + y + z, x * y * z

a, b = cal_sum_prod(4, 3, 2)
print('Sum', a)
print('Product', b)