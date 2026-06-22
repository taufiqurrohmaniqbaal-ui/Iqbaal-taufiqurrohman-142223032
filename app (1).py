
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard KDMP", layout="wide")

st.title("Dashboard Data KDMP")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("KDMP.csv")
    except:
        st.warning("Upload file CSV terlebih dahulu.")
        st.stop()

st.subheader("Preview Data")
st.dataframe(df.head(100))

st.write("Jumlah Baris:", len(df))
st.write("Jumlah Kolom:", len(df.columns))

st.subheader("Informasi Kolom")
st.write(df.dtypes)

kolom = st.selectbox("Pilih Kolom", df.columns)

if kolom:
    st.subheader(f"Analisis Kolom: {kolom}")
    st.write(df[kolom].describe(include="all"))

    if df[kolom].dtype == "object":
        st.bar_chart(df[kolom].value_counts().head(20))
    else:
        st.line_chart(df[kolom])

st.download_button(
    "Download Data",
    data=df.to_csv(index=False),
    file_name="hasil_export.csv",
    mime="text/csv"
)
