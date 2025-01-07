import requests
def weather(city_name,api_key):
  try:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()  
        weather=data['weather'][0]['description']
        temperature=data['main']['temp']
        humidity=data['main']['humidity']
        wind_speed=data['wind']['speed']
        print(f"weather{city_name}:")
        print(f"status{weather}")
        print(f"temperature:{temperature}°C")
        print(f"humidity:{humidity}%")
        print(f"wind speed:{wind_speed}")
    else:
        print("shahre morede nazar yaft nashod")
  except Exception as e:
    print("khata dar daryafte etelaat", e)
city_name=input("name shahr ra vared konid")
api_key="b809a595f6649fd29a66c7a0d7ff96fc"  
weather(city_name,api_key)