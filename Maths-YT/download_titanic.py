import urllib.request
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
out = 'titanic.csv'
urllib.request.urlretrieve(url, out)
print('Saved', out)
