# WindArrow
Plot Wind Arrow 2D plot - length based on wind intensity and angle based in wind direction.

## Usage

```python
import numpy as np
import matplotlib.pyplot as plt
from wind import windplot

days = np.array([ 0, 1, 2, 3, 4, 5, 6])
windv = np.array([ 5, 10, 15, 20, 25, 30, 35])
angles = np.array([45,275,190,100,280,18,45])

arrs = []
for j in enumerate(days):
    i = j[0]
    val = arrow(days[i], windv[i], angles[i])
    arrs.append(val)

f, ax = plt.subplots()
for i in arrs:
    ax.add_patch(i)

ax.grid(True)
ax.set_xlim(0,1.2*np.max(days))
ax.set_ylim(0,10)

plt.show()
```
