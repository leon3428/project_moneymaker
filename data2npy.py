import numpy as np
import os
import pandas as pd

files = os.listdir(os.getcwd() + '/saves')
df = pd.read_csv('dataset.csv')

#print(df.tail())
#print(df['O_1'])


def main():
    out = []
    y_data = []
    for filename in os.listdir(os.getcwd() + '/saves'):
        f = open(os.path.join(os.getcwd()+'/saves', filename), 'r')
        data = f.read()
        f.close()
        data = data.split('\n')[:-1]

        start = int(filename[9:-4])

        for i in range(0, len(data), 6):
            match = start + int(i/6)
            if match > 2279:
                return
            date = df['DATE'][match]
            date = date.split()[0]

            line = data[i]
            line = line.split()

            if date != line[1]:
                print('error')
                print(date, line[1])
                pass

            Ox = df['X'][match]
            Oh = df['1'][match]
            Oa = df['2'][match]
            try:
                odds = [Oh, Ox, Oa]
                odds = list(map(float, odds))
            except:
                print('error', match)

            goal_h = df['H'][match]
            goal_a = df['A'][match]
            y = [0]*6
            if goal_h > goal_a:
                y[0] = 1
                y[1] = 1
            if goal_a > goal_h:
                y[3] = 1
                y[4] = 1
            if goal_a == goal_h:
                y[1] = 1
                y[4] = 1
                y[2] = 1
            y_data.append(y)
            #print(y)
            #print(odds)

            home = data[i].split()[0]
            home_pol = list(map(int, data[i+1].split()))
            home_sub = list(map(int, data[i+2].split()))
            away = data[i+3].split()[0]
            away_pol = list(map(int, data[i+4].split()))
            away_sub = list(map(int, data[i+5].split()))


            h_o_c = [0]*4
            h_s_c = [0]*4
            a_o_c = [0]*4
            a_s_c = [0]*4
            if len(home_pol) != len(home_sub):
                print('error')
                print(len(home_pol), len(home_sub))
            for j in range(len(home_pol)):
                pol = home_pol[j] / 1000
                sub = home_sub[j] / 1000
                cat = 0
                if pol > -0.5 and pol <= 0:
                    cat = 1
                if pol > 0 and pol <= 0.5:
                    cat = 2
                if pol > 0.5:
                    cat = 3
                if sub > 0:
                    h_s_c[cat]+=1
                else:
                    h_o_c[cat]+=1

            for j in range(len(away_pol)):
                pol = away_pol[j] / 1000
                sub = away_sub[j] / 1000
                cat = 0
                if pol > -0.5 and pol <= 0:
                    cat = 1
                if pol > 0 and pol <= 0.5:
                    cat = 2
                if pol > 0.5:
                    cat = 3
                if sub > 0:
                    a_s_c[cat]+=1
                else:
                    a_o_c[cat]+=1

            twdata = h_o_c + h_s_c + a_o_c + a_s_c
            twdata = [round(x / len(home_pol), 2) for x in twdata]
            twdata = odds + twdata

            out.append(twdata)




            #print(twdata)
    out = np.array(out)
    y_data = np.array(y_data)
    print(out.shape, y_data.shape)
    np.save('x_data.npy', out)
    np.save('y_data.npy', y_data)



if __name__ == "__main__":
    main()
