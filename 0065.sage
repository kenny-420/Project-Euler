l = continued_fraction(e).convergents()
n = l[100-1].numerator()
print(sum([int(i) for i in str(n)]))
