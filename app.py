
import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans

st.title("Customer Segmentation Dashboard")

df = pd.read_csv("customer_data_100.csv")

st.subheader("Dataset")
st.dataframe(df)

st.subheader("Statistik Deskriptif")
st.write(df.describe())

fig = px.histogram(df, x="SpendingScore")
st.plotly_chart(fig, use_container_width=True)

st.subheader("K-Means Clustering")
k = st.slider("Jumlah Cluster", 2, 6, 3)

X = df[["AnnualIncome", "SpendingScore"]]

model = KMeans(n_clusters=k, random_state=42)
df["Cluster"] = model.fit_predict(X)

fig2 = px.scatter(
    df,
    x="AnnualIncome",
    y="SpendingScore",
    color=df["Cluster"].astype(str),
    hover_data=["CustomerID"]
)

st.plotly_chart(fig2, use_container_width=True)
st.dataframe(df)
