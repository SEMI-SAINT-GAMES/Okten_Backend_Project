import requests


def get_models():
    try:
        res = requests.get("https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/all-vehicles-model/records?limit=100&refine=make%3A%22Chevrolet%22")
        data = res.json()['results']
        for mod in data:
            print(mod['model'])
    except Exception as err:
        print(err)