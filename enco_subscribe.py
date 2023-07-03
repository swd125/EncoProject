import requests
from dotenv import dotenv_values

env = dotenv_values(".env")

enco_host = env.get('ENCO_CHIRPSTACK_HOST')
auth_key = env.get('ENCO_CHIRPSTACK_AUTH_KEY')
api_token = env.get('ENCO_CHIRPSTACK_API_TOKEN')
display_name = env.get('ENCO_CHIRPSTACK_DISPLAY_NAME')

def get_app_topics():

    get_orgs = requests.get(f'{enco_host}/api/organizations?limit=1&search={display_name}', headers={auth_key: api_token})
    get_org_id = get_orgs.json().get('result')[0].get('id') if get_orgs.json().get('result') else 0

    get_apps = requests.get(f'{enco_host}/api/applications?limit=1000&organizationID={get_org_id}', headers={auth_key: api_token})
    get_apps_list = get_apps.json().get('result')

    topic_list = []
    for app in get_apps_list:
        appID = app.get('id')
        get_devices = requests.get(f'{enco_host}/api/devices?limit=100&applicationID={appID}', headers={auth_key: api_token})
        get_deives_list = get_devices.json().get('result', [])

        for device in get_deives_list:
            devEui = device.get('devEUI')
            topic = f'application/{appID}/device/{devEui}/event/up'
            topic_list.append(topic)

    return topic_list


if __name__ == '__main__':
    get_app_topics()