def sum_chain(x=0):
    f = x

    def g(b=0):
        nonlocal f
        if not b:
            return f
        else:
            f += b
        return g
    return g


print(sum_chain())
