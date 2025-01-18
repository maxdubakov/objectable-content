import numpy as np
from pandas import DataFrame

# -------- basic example -----------------------------------------------------------------------------------------------

x, y, z = 1, 2, 3 # some Python boxed primitive variables

# oh, I need to multiply each of them by 2

# 1. put them in a "restricted computation domain"
values = np.array([x, y, z])

# 2. compute
values *= 2 # here, numpy operates on the level of unboxed variables, i.e. int64 in C. So, it can parallalize it as it thinks optimal

# 3. put it back to boxed
x, y, z = values


# -------- pd.DataFrame & class example --------------------------------------------------------------------------------

class Resistor:
    def __init__(self, number, manufacturer, resistance):
        self.number = number
        self.manufacturer = manufacturer
        self.resistance = resistance


class Product:
    def __init__(self, *components):
        # index=[...] actually puts these in computational domain where it's implemented as numpy array
        self.components = DataFrame([
            [c.manufacturer, c.resistance]
            for c in components
        ], columns=['manufacturer', 'resistance'], index=[c.number for c in components])

    def __getitem__(self, number):
        c = self.components.loc[number] # using computational domain to efficiently get item
        return Resistor(number, c.manufacturer, c.resistance) # back to boxed Python objects


p = Product(
    Resistor('10-1', 'honhai', 1),
    Resistor('10-2', 'honhai', 5),
    Resistor('10-3', 'honhai', 10),
)

print(f'{p.components.resistance.mean() = }')
print(f'{p["10-1"]}')
