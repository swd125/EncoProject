import requests

auth_key = 'Grpc-Metadata-Authorization'
api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5X2lkIjoiM2NjYmIwYzUtNWY0Yy00MmI1LWJiYmEtYTBmZTg3YmZlYjMxIiwiYXVkIjoiYXMiLCJpc3MiOiJhcyIsIm5iZiI6MTY4Nzc1NDU2Miwic3ViIjoiYXBpX2tleSJ9.bwoKdc3kZw8d3LeJx_DjLWwydyiz2jq35fgZJOePCBI'
display_name = 'EnCo'

def get_app_topics():

    get_orgs = requests.get(f'http://3.1.189.234:8081/api/organizations?limit=1&search={display_name}', headers={auth_key: api_token})
    get_org_id = get_orgs.json().get('result')[0].get('id') if get_orgs.json().get('result') else 0
    # print(get_orgs.status_code)
    # print(get_orgs.json())
    # print(f"{get_org_id = }")

    get_apps = requests.get(f'http://3.1.189.234:8081/api/applications?limit=1000&organizationID={get_org_id}', headers={auth_key: api_token})
    get_apps_list = get_apps.json().get('result')
    # print(get_apps_list)

    result_list = []
    topic_list = []
    for app in get_apps_list:
        appID = app.get('id')
        get_devices = requests.get(f'http://3.1.189.234:8081/api/devices?limit=100&applicationID={appID}', headers={auth_key: api_token})
        get_deives_list = get_devices.json().get('result', [])

        for device in get_deives_list:
            devEui = device.get('devEUI')
            topic = f'application/{appID}/device/{devEui}/event/up'
            topic_list.append(topic)

    return topic_list


if __name__ == '__main__':
    get_app_topics()