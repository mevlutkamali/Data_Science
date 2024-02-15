
# Libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

source = pd.read_csv('sourceMissing.csv')
print(source)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

age = source.iloc[:, 1:4].values
print(age) 

imputer = imputer.fit(age[:, 1:4])
age[:, 1:4] = imputer.transform(age[:, 1:4])
print(age)

print("Finish. . .")

# fit() fonksiyonu veriyi eğitmek için kullandığımız fonksiyondur.
# transform() fonk. ile ögrendiği bilgiyi uygulamasını istiyoruz.

# Burada eksik olan sayısal verierin ortalamasını hesaplatıp eksik olan sayısal veri dizisine yazdırdık.