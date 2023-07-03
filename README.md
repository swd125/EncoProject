# EncoProject

# 1. Install Requirement
```bash
pip freeze -r requirement.txt
```

# 2. Create .env
```bash
touch .env
```

# 3. Set Keys and Values in .env
```bash
INFLUXDB_USERNAME = 
INFLUXDB_PASSWORD = 
INFLUXDB_ORG = 
INFLUXDB_BUCKET = 
INFLUXDB_API_TOKEN = 


# /home/swd125/Desktop/Python/EncoProject/enco_subscribe.py
ENCO_CHIRPSTACK_HOST = 
ENCO_CHIRPSTACK_AUTH_KEY = 
ENCO_CHIRPSTACK_API_TOKEN = 
ENCO_CHIRPSTACK_DISPLAY_NAME = 


# /home/swd125/Desktop/Python/EncoProject/influxdb.py
INFLUXDB_HOSTNAME = 
INFLUXDB_PORT = 
INFLUXDB_TOKEN = 
INFLUXDB_BUCKET = 
INFLUXDB_ORG = 


# /home/swd125/Desktop/Python/EncoProject/mqtt_subscription_v1.py
ENCO_MQTT_BROKER = 
ENCO_MQTT_PORT = 
ENCO_MQTT_CLIENT_ID = 
ENCO_MQTT_TOPIC = 

ENCO_IOT_CORE_BROKER = 
ENCO_IOT_CORE_PORT = 
ENCO_IOT_CORE_CLIENT_ID = 
ENCO_IOT_CORE_TOPIC = 
ENCO_IOT_CORE_TSL_CA_CERTS = 
ENCO_IOT_CORE_TSL_CERT_FILE= 
ENCO_IOT_CORE_TSL_KEY_FILE = 
```

# 4. Run main.py 
> for Mqtt doesn't sent param

> for Iot-Core sent param = "iot_core"
```bash
python main.py [param]
```
