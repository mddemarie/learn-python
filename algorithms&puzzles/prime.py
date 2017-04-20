def is_prime(x):
    if x <= 0:
        raise ValueError("You passed a negative number!")
    elif x > 1:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True
    else:
        return False
print(is_prime(3))