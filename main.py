import streamlit as st

st.title("Pronóstico del tiempo para los próximos días")
place =st.text_input("Lugar: ")
days = st.slider("Días a pronosticar",
                 min_value=1,
                 max_value=5,
                 help="Selecciona el número de días a pronosticar")
option = st.selectbox("Selecione los datos a ver",
                      ("Temperatura", "Cielo"))

st.subheader(f"{option} para los próximos {days} días en {place}")
