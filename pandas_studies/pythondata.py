import pandas as pd
import pydataset
import matplotlib.pyplot as plt


set = pydataset.data('cancer')
print(set)

plt.plot(set['wt.loss'])
plt.show()

