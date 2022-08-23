import streamlit as st
import pandas as pandas
import numpy as np 

velocidade=59
temp_cvt=34
combustivel=1

# def get_data():
    # pd.read_csv()
    # or
    # read JSON
    # return data

st.set_page_config(
    page_title="Dashboard Fox Baja",
    page_icon="🦊",
    layout="wide"
)

st.title('Dashboard Fox Baja')
st.columns(3)

kpi1, kpi2, kpi3 = st.columns(3)

# Velocidade:
kpi1.metric(
    label="Velocidade",
    value=int(velocidade)
)

# Temperatura:
kpi2.metric(
    label="Temperatura da CVT",
    value=int(temp_cvt)
)

# Gasolina:
kpi3.metric(
    label="Nivel de combustivel",
    value=combustivel
)



fig_vel, fig_temp = st.columns(2)

