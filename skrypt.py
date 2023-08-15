# nowy program
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('Baza.csv')
df2= df.iloc[:,[0, 1, 4, 5, 6, 7]]
# ART = df2[np.logical_and(np.logical_and(df2['SEGMENT_ALIAS'] == '08600 Działalność podstawowa (bez paliwa)',df2['INDICATEUR'] == 'Artykuły'), df2['Sklep'] == '001 Piaseczno')]
ART = df2[(df2['SEGMENT_ALIAS'] == '08600 Działalność podstawowa (bez paliwa)') & (df2['INDICATEUR'] == 'Artykuły') & (df2['Sklep'] == '001 Piaseczno')]
# print(ART)
ART2= ART.sort_values('Data', ascending = True)
print(ART2)
plt.plot(ART2['Data'], ART2['Realise'] )
plt.xlabel("Data")
plt.ylabel("Artykuły")
plt.title("Sprzedaż artykułów w czasie")
plt.yticks([3000000, 3500000, 4000000, 4500000, 5000000, 5500000, 6000000],
           [ '3 mln', '3,5 mln', '4 mln', '4,5 mln', '5 mln', '5,5 mln', '6 mln'])
plt.xticks(rotation = 45)
plt.show()
# yttyty
# tytyt
# yty
# typety
# typeyty
