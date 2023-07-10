import requests
def get_exchange_rate(base_currency, target_currency):
    api_key = '46c0ac43210e14967953fabb97a3bd2b'  # Replace with your actual Fixer API key
    url = f'http://data.fixer.io/api/latest?access_key={api_key}&base={base_currency}&symbols={target_currency}'
    response = requests.get(url)
    data = response.json()
    print(data)
    return data['rates'][target_currency]

