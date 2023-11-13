import requests
from datetime import date

# from apps.users_requests.models import CurrencyModel



def fetch_currency_data():
    try:
        response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
        data = response.json()
        return data
    except Exception as err:
        print(err)
        return

# def update_currency_rates():
#     data = fetch_currency_data()
#     #for fromCur, toCur, buy, sale in data[0]:
#     CurrencyModel.objects.update_or_create(fromCur=data[0]["ccy"], toCur=data[0]["base_ccy"], buy=data[0]["buy"], sale=data[0]["sale"])
#     CurrencyModel.objects.update_or_create(fromCur=data[1]["ccy"], toCur=data[1]["base_ccy"], buy=data[1]["buy"], sale=data[1]["sale"])