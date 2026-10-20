import matplotlib.pyplot as plt

labels=["CSE","IT","ECE","EEE"]
values=[120,90,80,60]

plt.pie(values,labels=labels,autopct="%1.1f%%")
plt.show()
