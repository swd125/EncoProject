from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from dotenv import dotenv_values

env = dotenv_values(".env")


class InfluxDB:
    localhost = env.get('INFLUXDB_HOSTNAME')
    port = env.get('INFLUXDB_PORT')
    token = env.get('INFLUXDB_TOKEN')
    bucket = env.get('INFLUXDB_BUCKET')
    org = env.get('INFLUXDB_ORG')

    def connect(self):
        client = InfluxDBClient(url=f"http://{self.localhost}:{self.port}", token=self.token, org=self.org)
        return client
    
    def write_json_data(self, json_data):
        write_api = self.connect().write_api(write_options=SYNCHRONOUS)
        write_api.write(org=self.org, bucket=self.bucket, record=json_data, write_precision=WritePrecision.NS)
        self.connect().close()
        return write_api


if __name__ == '__main__':

    mock_data = {
        'topic': 'application/28/device/24e124136b231037/event/up', 
        'result': {
            'applicationID': '28', 
            'applicationName': 'EM300_SLD', 
            'deviceName': 'women_toilet_A_G_leak', 
            'deviceProfileName': 'EM300_SLD', 
            'deviceProfileID': '78ce1430-0eb6-4e4f-825a-5e6fba987e75', 
            'devEUI': '24e124136b231037', 
            'rxInfo': [
                {
                    'gatewayID': '7276ff00450402f6', 
                    'uplinkID': 'b97edbb1-e652-4cc0-86f9-83373c9155a4', 
                    'name': 'enco_building_A', 
                    'time': '2021-12-24T22:04:00.809782Z', 
                    'rssi': -84, 
                    'loRaSNR': 8.2, 
                    'location': {
                        'latitude': 0, 
                        'longitude': 0, 
                        'altitude': 0
                    }
                }
            ], 
            'txInfo': {
                'frequency': 922200000, 
                'dr': 2
            }, 
            'adr': True, 
            'fCnt': 104934, 
            'fPort': 85, 
            'data': 'A2cKAQRoeAUAAQ==', 
            'object': {
                'humidity': 55.5, 
                'temperature': 27.7, 
                'water_leak': 'leak'
            }
        }
    }

    json_body = {
        "measurement": mock_data['result']['applicationName'],
        "tags": {
            "deviceName": mock_data['result']['deviceName'],
            "devEUI": mock_data['result']['devEUI'],
        },
        # "time": "2009-11-10T23:00:00Z",
        "fields": {
            "humidity": mock_data['result']['object']['humidity'],
            "temperature": mock_data['result']['object']['temperature'],
            "water_leak": mock_data['result']['object']['water_leak'],
        }
    }

    data = InfluxDB().write_json_data(json_body)
    print(data)