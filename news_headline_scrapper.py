import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://bbc.com/news"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code != 200:
    print(f"Failed to connect to BBC News. Status code: {response.status_code}")
    exit()

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <h2> tags which typically contain headlines
headlines = soup.find_all('h2')

# Prepare file name with current date and time
current_datetime = datetime.now().strftime("%H:%M:%S_%d-%m-%Y")
file_name = f"Today_News_{current_datetime}.txt"

# Write headlines to the file
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(f"Top 25 News Headlines from BBC News:\n\n")
    for idx, headline in enumerate(headlines[:25], start=1):
        file.write(f"{idx}. {headline.text.strip()}\n")

print(f"Top 25 news headlines saved to '{file_name}'")

