
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns

iris = load_iris()

features = iris.feature_names

X = iris.data
X.shape

y = iris.target
y.shape

i = 3  # the i factor is just for the visualization of the particular feature using the box plot. ranges from 0 to 3.
sns.boxplot(x=iris.target, y=iris.data[:, i])
title = "Class Variation With Respect to " + features[i]
plt.title(title)
plt.xlabel("Output Class")
plt.ylabel(features[i])
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

print(lin_model.coef_)
weights = lin_model.coef_
print("Most important feature is :", features[abs(weights).argmax()])
print("Least Imporant feature is:", features[abs(weights).argmin()])

print(lin_model.score(X_test, y_test))
