import requests
import pandas as pd
import jsonstat
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

url = ('http://www.cso.ie/StatbankServices/StatbankServices.svc/jsonservice/responseinstance/TEM20')
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ':', value)

print(json_data.keys())
data = jsonstat.from_url(url)
print(data)
mcar = data.dataset(0)
print(mcar)
df = mcar.to_data_frame()
print(df.head(10))
print(df.tail(10))
print(df.dtypes)
print(df.sort_values("Make and Model", ascending=False))
Car = df['Make and Model']
print(Car)
print(max(Car))
print(min(Car))
print(list(Car))
df1 = df['Make and Model'].value_counts()
print(df.shape)
#print(df["Make and Model"].describe())
print(df.iloc[:,1])
print(df.dtypes)
print(df.loc[100:120, "Month":"Make and Model"])
print(df.iloc[220:230, 2:4])
print(df.iloc[30000])
print(df.sort_values("Value", ascending=False))

is_LA = df["Statistic"] == ("New Private Cars Licensed for the First Time")
is_S = df["Make and Model"] == "Mercedes Benz E Class"
MBE = df[is_LA & is_S]
print(MBE)
x = MBE["Month"].tail(6)
y = MBE["Value"].tail(6)
plt.bar(x,y)
plt.show()
is_LA = df["Statistic"] == ("New Private Cars Licensed for the First Time")
is_S = df["Make and Model"] == "Mercedes Benz C Class"
MBC = df[is_LA & is_S]
fig, ax = plt.subplots()
ax.plot(MBC["Month"].tail(6), MBC["Value"].tail(6),color='r')
ax.set_xlabel("Month")
ax.set_ylabel("Registrations")
ax.set_title('Mercedes Bens C-Class')
plt.show()
is_LA = df["Statistic"] == ("New Private Cars Licensed for the First Time")
is_S = df["Make and Model"] == "Landrover Range Rover"
RR = df[is_LA & is_S]
fig, ax = plt.subplots()
ax.plot(RR["Month"].tail(6), RR["Value"].tail(6),color='g', marker="v", linestyle="--")
ax.set_xlabel("Month")
ax.set_ylabel("Registrations")
ax.set_title('Landrover Range Rover')
plt.show()
print(df.head())
df2f = df.drop(["Value", "Statistic"], axis=1)
print(df2f)
print(df.keys())
print(mcar.value(C03398V04090='Audi A3'))
print(mcar.value(C03398V04090='Volkswagen Golf'))
print(df["Month"])
print(len("Make and Model"))
car = df['Make and Model']
print(max(car))
print(min(car))
finalcarList=np.unique(car).tolist()
print(finalcarList)
c2 = df.groupby("Make and Model")["Month"].max()
print(c2.head(10))
