from fuzzy_logic import rules
sum_mf = [1, 1, 3, 5]
D = rules(sum_mf)
print(D)

''''#print(values)
            points1 = [0, 0, 0, 0.5]
            points2 = [0.4, 0.5, 0.6, 0.7]
            points3 = [0.6, 0.7, 0.8, 0.9]
            points4 = [0.8, 1, 1, 1]
            mf = []
            i = 0
            while i < len(values):
                membf = [trapmf(values[i], points1), trapmf(values[i], points2), trapmf(values[i], points3),
                         trapmf(values[i], points4)]
                mf.append(membf)
                i += 1
            #print(mf)
            sum_mf = [0, 0, 0, 0]
            i = 0
            while i < len(mf):
                j = 0
                while j < 4:
                    sum_mf[j] += mf[i][j]
                    j += 1
                i += 1
            D = rules(sum_mf)
            print('Дисциплина', D)'''