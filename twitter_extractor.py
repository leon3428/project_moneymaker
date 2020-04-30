import pandas as pd
from tqdm import tqdm

df = pd.read_csv('dataset.csv')
f = open('clubs.txt', 'r')

print(df.head())
names = f.read()
names = names.split('\n')
names.pop()

for index, row in tqdm(df.iterrows()):
    date = row.DATE
    date = date.split()[0]
    home = ""
    away = ""
    for club in names:
        club = club.split()
        try:
            a = int(club[1])
        except:
            club = [club[0] + ' ' + club[1], club[2], club[3]]
        #print(club)
        if row.HOME == club[0]:
            home = club[2]
        if row.AWAY == club[0]:
            away = club[2]
    print(home, away)

    break

f.close()
