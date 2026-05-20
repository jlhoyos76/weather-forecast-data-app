import streamlit as st
import plotly.express as px
from backend import get_data

#Añade titulo, caja de texto, slider, selector y subheader
st.title("Pronóstico del tiempo")
place =st.text_input("Lugar: ",
                 help="Escribe el nombre de la localidad")
days = st.slider("Días a pronosticar",
                 min_value=1,
                 max_value=5,
                 help="Selecciona el número de días a pronosticar")
option = st.selectbox("Selecione los datos a ver",
                      ("Temperatura", "Cielo"))

st.subheader(f"{option} para los próximos {days} días en {place}")

if place:
    #Obtenemos los datos de la API
    filtered_data = get_data(place, days)

    if option=="Temperatura":
        temperaturas = [dict["main"]["temp"] for dict in filtered_data]
        fechas = [dict["dt_txt"] for dict in filtered_data]
        # Crea el plot de temperatura
        figure = px.line(x=fechas,y=temperaturas, labels={"x": "Fecha", "y": "Temperatura (ºC)"})
        st.plotly_chart(figure)

    if option == "Cielo":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]

        st.image(image_paths, width=85)