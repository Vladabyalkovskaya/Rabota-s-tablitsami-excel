import pandas as pd
a = pd.read_excel('phone_numbers.xlsx')
b = []
c = 0
f = ''
g = "0123456789"
k = []
def listeds(x, y):
  for i in range(len(x)):
    y.append(str(x.iloc[i]))

  for i in range(len(y)):
    for j in range(len(y[i])):
      if y[i][j] not in g:
        y[i] = y[i].replace(y[i][j], '.')


def create_df(a, b,f,k):
  for i in range(len(b)):
    for j in range(len(b[i])):
      if b[i][j] != ".":
        f = f + b[i][j]
    k.append(int(f))
    f = ''
  for i in range(len(k)):
    k[i] = int(k[i])
