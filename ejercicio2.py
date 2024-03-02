from sklearn.linear_model import LinearRegression
from os import system as system

X_train=[[1],[2],[3],[4],[5],[6],[7],[8]]

y_train=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

model=LinearRegression()
model.fit(X_train, y_train)

system("cls")

km=int(input ("ingrese el valor en kilometos: "))

km_to_convert=[[km]]
predict_m=model.predict(km_to_convert)


print(f"{km}  kilometros equivalente aproximadamente a {predict_m[0]} metros")