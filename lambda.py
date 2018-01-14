def make_repeater(n):
    return lambda s:s*n*n

twice=make_repeater(2)

print twice('word')
print twice(5)
