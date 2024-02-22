import os
import tarfile
from six.moves import urllib
import pandas as pd

#the way of finding the data
ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
PATH = os.path.join("datasets", "housing")
URL = ROOT + "datasets/housing/housing.tgz"

#function to fetch the data
def fetch_data(housing_url = URL, housing_path = PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path = housing_path)
    housing_tgz.close()


#return a pandas dataframe object containing all the data
def load_data(housing_path = PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)
