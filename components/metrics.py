import streamlit as st


def metric_row(metrics):

    cols = st.columns(len(metrics))

    for col, metric in zip(cols, metrics):

        col.metric(
            metric["label"],
            metric["value"]
        )