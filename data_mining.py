
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("customer_data_100.csv")

X = df[["AnnualIncome", "SpendingScore"]]

model = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = model.fit_predict(X)

print(df.head())
df.to_csv("hasil_clustering.csv", index=False)
print("Hasil disimpan ke hasil_clustering.csv")
