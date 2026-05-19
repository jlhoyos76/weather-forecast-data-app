import streamlit as st
import plotly.express as px
from backend import get_data()


st.title("Pronóstico del tiempo para los próximos días")
place =st.text_input("Lugar: ")
days = st.slider("Días a pronosticar",
                 min_value=1,
                 max_value=5,
                 help="Selecciona el número de días a pronosticar")

option = st.selectbox("Selecione los datos a ver",
                      ("Temperatura", "Cielo"))

st.subheader(f"{option} para los próximos {days} días en {place}")



data = get_data(place, days, option) # devuelve 2 listas

# Se puede usar un objeto gráfico Plotly o Bokeh. Son bibliotecas de visualización de datos
figure = px.line(x=d,y=t,labels={'x':"Días",'y':"Temperatura (ºC)"})
st.plotly_chart(figure)