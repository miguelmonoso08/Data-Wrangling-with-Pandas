import pandas as pd

a = {"Student": ["Ice Bear","Panda","Grizzly"],
     "Math": [80,95,79]}
a = pd.DataFrame (a, columns = ["Student","Math"])

b = {"Student": ["Ice Bear","Panda","Grizzly"],
     "Electronics": [85,81,83]}
b = pd.DataFrame (b, columns = ["Student","Electronics"])

c = {"Student": ["Ice Bear","Panda","Grizzly"],
     "GEAS": [90,79,93]}
c = pd.DataFrame (c, columns = ["Student","GEAS"])

d = {"Student": ["Ice Bear","Panda","Grizzly"],
     "ESAT": [93,89,88]}
d = pd.DataFrame (d, columns = ["Student","ESAT"])

e = pd.merge (a,b, how="outer", on="Student")

f = pd.merge (e,c, how="outer", on="Student")

print(" ")
g = pd.merge(f,d, how="outer", on="Student")
print(g)
print(" ")

longformat = pd.melt(g, id_vars = "Student", 
                     value_vars = ["Math","Electronics","GEAS","ESAT"])

print(longformat.rename(columns={"variable": "Subject","value": "Grades"}))


