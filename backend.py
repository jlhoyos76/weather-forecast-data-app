import requests

API_KEY = "be81f8932037b5276f7e72ae833266dc"

def get_data(place, forecast_days=None, kind=None):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response=requests.get(url)
    data = response.json()

    filtered_data = data["list"] # cargamos la lista de datos.
    # Son 40 tomas de datos porque arroja temperatura cada 3h. 1 día son 8 tomas de datos

    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if kind=="Temperatura":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    elif kind=="Cielo":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__=="__main__":
    print(get_data(place="Bargas", forecast_days=3, kind="Temperatura"))