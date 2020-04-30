import pandas as pd

df = pd.read_excel ('data.xlsx')
df = df[(df.ID == 'ENG PL') & ((df.SEASON == '2018/2019') | (df.SEASON == '2017/2018') | (df.SEASON == '2016/2017') | (df.SEASON == '2015/2016') | (df.SEASON == '2014/2015') | (df.SEASON == '2013/2014'))]
print (df.head())
print(df.shape, df.shape[0]/380)

df = df.drop('ID', 1)
df.to_csv('dataset.csv', index = False)

"""
names = set([])

for index, row in df.iterrows():
    names.add(row.HOME)
    names.add(row.AWAY)

print(names)

f = open("clubs.txt", "w")

for i, name in enumerate(names):
    print(name, 'hashtag: ', end = '')
    hash = input()
    f.write(name + ' ' + str(i) + ' ' + hash + '\n')

f.close()
"""
