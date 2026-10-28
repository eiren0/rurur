from sklearn.datasets import load_iris

from sklearn.neighbors import KNeighborsClassifier


iris = load_iris()

model = KNeighborsClassifier(n_neighbors=3)

model.fit(iris.data, iris.target)


new_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_flower)

print("Модель определила класс цветка:", iris.target_names[prediction[0]])
