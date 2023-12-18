import pandas as pd
from func import listeds
from func import create_df
a = pd.read_excel('phone_numbers.xlsx')
b = []
f = ''
g = "0123456789"
k = []
listeds(a,b)
create_df(a,b,f,k)
df = pd.DataFrame({"phone number" : k})
print(df)
writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer)
writer.close()

