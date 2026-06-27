import streamlit as st
import pandas as pd
from services.data_importer import import_drawings_from_csv

st.title("📥 Data Import")

st.write("Upload a lottery CSV file with these columns:")
st.code("draw_date,n1,n2,n3,n4,n5,bonus")

game = st.selectbox("Choose game", ["Mega Millions", "Powerball"])

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview")
    st.dataframe(df, width="stretch")

    if st.button("Import to ORACLE Database"):
        temp_path = "downloads/uploaded_drawings.csv"
        df.to_csv(temp_path, index=False)

        import_drawings_from_csv(temp_path, game)

        st.success(f"{game} drawings imported successfully!")