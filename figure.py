import matplotlib.pyplot as plt

data = [0.455,0.123,0.078,0.344]
x_0 = [1,0,0,0]
plt.figure(figsize=(10,10))

labels = '1','2','3','4'

colors = ['pink','green','blue','yellow']

plt.pie(data , radius=1.0,pctdistance = 0.8, labels = labels ,colors = colors, startangle=0,autopct='%1.1f%%')
plt.pie(x_0, radius=0.6,colors = 'w')
plt.show()