import download_data

download_data.fetch_data()
housing = download_data.load_data()

print(housing.head(10))
print('~'*30)
print(housing.info())
print('~'*30)
print(housing["ocean_proximity"].value_counts())
print('~'*30)
print(housing.describe())
print('~'*40)

import matplotlib.pyplot as plt
housing.hist(bins = 5, figsize = (20,15))
plt.show()
