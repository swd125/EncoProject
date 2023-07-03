import sys
from mqtt_subscription import run_mqtt_subscription as run
from mqtt_subscription_v1 import Mqtt_Subscription_v1
from dotenv import dotenv_values

env = dotenv_values(".env")

# # ---- Enco Mqtt ----
# broker = env.get('ENCO_MQTT_BROKER')
# port = env.get('ENCO_MQTT_PORT')
# client_id = env.get('ENCO_MQTT_CLIENT_ID')
# topic = env.get('ENCO_MQTT_TOPIC')

# # ---- IOT Core ----
# broker = env.get('ENCO_IOT_CORE_BROKER')
# port = env.get('ENCO_IOT_CORE_PORT')
# client_id = env.get('ENCO_IOT_CORE_CLIENT_ID')
# topic = env.get('ENCO_IOT_CORE_TOPIC')
# tsl = {
#     "ca_certs" : env.get('ENCO_IOT_CORE_TSL_CA_CERTS'),
#     "certfile" : env.get('ENCO_IOT_CORE_TSL_CERT_FILE'),
#     "keyfile"  : env.get('ENCO_IOT_CORE_TSL_KEY_FILE'),
# }

if __name__ == '__main__':

    # ---- Enco Mqtt ----
    broker = env.get('ENCO_MQTT_BROKER')
    port = env.get('ENCO_MQTT_PORT')
    client_id = env.get('ENCO_MQTT_CLIENT_ID')
    topic = env.get('ENCO_MQTT_TOPIC')
    tsl = {}
    
    if len(sys.argv) > 1 and sys.argv[1] == 'iot_core':
        # ---- IOT Core ----
        broker = env.get('ENCO_IOT_CORE_BROKER')
        port = env.get('ENCO_IOT_CORE_PORT')
        client_id = env.get('ENCO_IOT_CORE_CLIENT_ID')
        topic = env.get('ENCO_IOT_CORE_TOPIC')
        tsl = {
            "ca_certs" : env.get('ENCO_IOT_CORE_TSL_CA_CERTS'),
            "certfile" : env.get('ENCO_IOT_CORE_TSL_CERT_FILE'),
            "keyfile"  : env.get('ENCO_IOT_CORE_TSL_KEY_FILE'),
        }

    port = int(port)
    
    client = Mqtt_Subscription_v1(broker, port, client_id, tsl)
    client.run_subscribe(topic)