def func(p):
    if p > 0:
        return str(p % 10) + func (p // 10)
    else:
        return ''

print(func(int(input())))