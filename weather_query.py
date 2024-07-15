countrycode = input("Enter The Country Code: ")
zipcode = input("Enter The Zip Code of Your Area: ")
apikey= "b5355a2d7ad8244605398797af15e581"

url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={apikey}"

import requests
import sys

result = requests.get(url)

if result.status_code==200:
    print(result.text)
else:
    print("EROORRR! Please chech Your Country Code OR Zip Code")
    sys.exit(1)
