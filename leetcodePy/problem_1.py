import matplotlib.pyplot as pl

nums = [value**2 for value in range(1, 10)]
pl.title("numbers")
pl.plot(nums)
pl.show()

