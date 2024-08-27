# import requests

    
# def get_weather(city):
#     api_key="7e6655d516cc0d5d24f0343a9cc8584b"
#     base_url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response=requests.get(base_url)
#     data=response.json()

#     if data["cod"]!="404":
#      main = data["main"]
#      weather= data["weather"] [0]
#      temperature=main["temp"]
#      description =weather["description"]
#      print(f"the temperature in {city}is {temperature} degree celsius with {description}.")
#     else:
#         print("city not found")
    
# def take_command(b):
# #  
#       city = b.replace('weather in','').strip()
#       print(f"the temperature in {city} is :")
    
# city=(input("enter city name :"))
# take_command(f"weather in {city}")
# get_weather(city)
# take_command() 

# import requests

# def get_weather(city):
#     api_key = "7e6655d516cc0d5d24f0343a9cc8584b"
#     base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#     response = requests.get(base_url)
#     data = response.json()

#     if data["cod"] != "404":
#         main = data["main"]
#         weather = data["weather"][0]
#         temperature = main["temp"]
#         description = weather["description"]  # Access the description key correctly
#         print(f"The temperature in {city} is {temperature}°C with {description}.")
#     else:
#         print("City not found.")

# def take_command(b):
#     # Assume 'b' is something like "weather in Mumbai"
#     city = b.replace('weather in', '').strip()
#     print(f"The temperature in {city} is:")

# # Get city name from user
# city = input("Enter city name: ")

# # Call functions
# take_command(f"weather in {city}")
# get_weather(city)

import requests

def get_weather(city):
    api_key = "7e6655d516cc0d5d24f0343a9cc8584b"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
     main = data["main"]
     weather = data["weather"][0]
     temperature = main["temp"]
     description = weather["description"]
     print(f"the temperature in {city} is {temperature} degree celsius with {description}")

    else:
       print("city not found")

def take_command(b):
   city = b.replace('weather in','').strip()

city = input("enter city name :")

get_weather(city)
take_command(f"weather in {city} is")