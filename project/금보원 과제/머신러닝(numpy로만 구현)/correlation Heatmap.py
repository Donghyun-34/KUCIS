import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('./creditcard.csv')
list_of_correlations= df.corr(method='pearson')
plt.figure(figsize=(11,7))
sns.heatmap(list_of_correlations,linewidths=0.005,linecolor='k')
plt.title('Correlation Heatmap')
plt.show()

print(np.abs(list_of_correlations['Class']).sort_values(ascending=False).head(13))