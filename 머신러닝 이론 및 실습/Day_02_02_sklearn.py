# scikit-learn, sklearn, matplotlib 설치
from sklearn import datasets, neighbors


iris = datasets.load_iris()
print(type(iris))
print(iris.keys())
# dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])

print(iris['target_names'])     #['setosa' 'versicolor' 'virginica']
print(iris['feature_names'])    #['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(iris['filename'])
print(iris['DESCR'])
print(iris['data'])
print(type(iris['data']))
print(iris['target'])


print(iris['data'].shape)
print(iris['target'].shape)
print(iris['target'])

print(iris['target_names'][:3])
print(iris['target_names'][[0, 1]])
print(iris['target_names'][iris['target']])
print()
def sk_2():
    iris = datasets.load_iris()

    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(iris.data, iris.target)

    preds = knn.predict(iris.data)
    print(preds)

    bools = (preds == iris.target)

    bools_sum = sum(bools)
    print('acc :', bools_sum / len(bools))



#sk_1()
sk_2()