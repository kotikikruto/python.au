import pandas
import matplotlib.pyplot as plt
from scipy import stats

df1 = pandas.read_csv("experiments.csv")  # Данные стоимости проезда в нескольких городах России на 2021 год
df2 = pandas.read_csv("experiments_upd.csv")  # Те же данные, но без учета Москвы и Санкт-Петербурга

df12 = pandas.DataFrame(data={
    'df1': df1['experiments'],
    'df2': df2['experiments'],
})

df12.plot.kde()

plt.show()

d1 = df12['df1']
d2 = df12['df2']

print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N=5000))
print(stats.kstest(d2, 'norm', (d2.mean(), d2.std()), N=5000))

# Второе распределение "Более нормальное"
