import requests

url = 'https://api.exchangerate-api.com/v4/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

b = data["base"]
d = data["date"]
r = data["rates"]["EUR"]
j = data["rates"]["JPY"]
c = data["rates"]["CAD"]


print("Monena Base: {}, \nFecha: {}, \nEuro: {}, \nYen: {}, \nDolar Canadiense: {}".format(b, d, r, j, c))