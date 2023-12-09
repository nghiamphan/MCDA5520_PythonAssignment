import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def display():
    uploaded_file = st.file_uploader("Choose a CSV file")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        figure = plt.figure(figsize=(10, 5))
        plt.hist(df["Age"])
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.title("Distribution of Ages")
        st.pyplot(figure)


display()
