import json
import ssl
import time
from paho.mqtt import client as mqtt_client

from clean_data import clean_data, make_influx_data
from enco_subscribe import get_app_topics
from influxdb import InfluxDB
from dotenv import dotenv_values

env = dotenv_values(".env")


broker = env.get('ENCO_MQTT_BROKER')
port = env.get('ENCO_MQTT_PORT')
client_id = env.get('ENCO_MQTT_CLIENT_ID')
topic = env.get('ENCO_MQTT_TOPIC')
topic_list = get_app_topics()


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        print("on_connect")
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client, topic):
    def on_message(client, userdata, msg):
        # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message_result = json.loads(msg.payload.decode())
        result = {"topic": msg.topic, "result": message_result}
        data = clean_data(topic_list, result)
        if data:
            make_data = make_influx_data(data)
            InfluxDB().write_json_data(make_data)
            print(make_data)
            print("---------------------")

    client.subscribe(topic)
    client.on_message = on_message
    return client.on_message


def run_mqtt_subscription():
    client = connect_mqtt()
    subscribe(client, topic)
    client.loop_forever()


if __name__ == '__main__':
    run_mqtt_subscription()
