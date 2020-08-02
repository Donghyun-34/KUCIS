import numpy as np
import pandas as pd

array = np.array([1, 2, 3, 4, 5, 6])
array1 = np.random.randint(10, 100, 10)
print(array1)

two_list = [['dongwook', 50, 86], ['junsub', 89, 70], ['jiyung', 99, 99]]

list2 = pd.read_csv('iphone.csv', index_col=0)
print(list2)