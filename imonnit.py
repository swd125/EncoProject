import requests
from dotenv import dotenv_values

env = dotenv_values(".env")
hostname = env.get('ENCO_IMONNIT_HOST')
api_key_id = env.get('ENCO_API_KEY_ID')
api_secret_key = env.get('ENCO_API_SECRET_KEY')

def getDataFromAPI():

    response = requests.post(f'{hostname}/json/SensorListFull', headers={"APIKeyID": api_key_id, "APISecretKey": api_secret_key})
    print(response.status_code)
    print(response.json())
    print(response)
    print('Yeah!!')


if __name__ == '__main__':
    getDataFromAPI()