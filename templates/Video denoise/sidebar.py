import streamlit as st

Models = {}

def show():

    inputs = {}
    with st.sidebar:
        st.write("## Model")
        model = st.selectbox("Which model", list(Models.keys()))
        if isinstance(model, dict):
            model_variant = st.selectbox("Which model variant", list(model.keys()))
            inputs = ["model_func"] = Models[model][model_variant]
        else:
            inputs = ["model_func"] = Models[model]