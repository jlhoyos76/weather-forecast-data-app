API_KEY = "be81f8932037b5276f7e72ae833266dc"

def get_data(place, forecast_days, kind):

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}& ppid={API_KEY}"
    
    return data