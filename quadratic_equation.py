from math import sqrt


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
<<<<<<< 059d50acda4cd0d0bc6861db0d57d394d61efbba
    root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    if discriminant == 0:
        return root1, None
    elif discriminant > 0 :
        return root1, root2
    else:
        return None, None
=======

    if discriminant == 0:
        root1 = - b / (2 * a)
        return root1, None

    elif discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        return None, None

print(get_roots(1, 2, -3))
>>>>>>> 613176c476297c74002862c2ca4d2a8ecc4ece90
