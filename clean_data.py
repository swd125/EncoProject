import datetime


def clean_data(app_list, message):
    topic = message.get('topic')
    result = message.get('result')
    keys_list = ['humidity', 'temperature', 'water_leak', 'adc1', 'adc2', 'chn25', 'chn26']

    if topic in app_list and result:
        if result.get('object'):
            for key, value in result['object'].items():
                if key in keys_list:
                    return message
    return {}

def make_influx_data(data):

    fields = {}
    json_body = []
    raw_data = {
        "measurement": data['result']['applicationName'],
        # "tags": {
        #     "deviceName": data['result']['deviceName'],
        #     "devEUI": data['result']['devEUI'],
        # },
        # "time": datetime.datetime.now(),
        # "fields": {
        #     "humidity": data['result']['object']['humidity'],
        #     "temperature": data['result']['object']['temperature'],
        #     "water_leak": data['result']['object']['water_leak'],
        # }
    }

    for key, value in data['result']['object'].items():
        
        raw_data.update({
            "tags": {
                "deviceName": data['result']['deviceName'],
                "devEUI": data['result']['devEUI'],
            }
        })
        
        if key == 'water_leak':
            fields[key] = 1 if value == 'leak' else 0
        elif key in ['din1', 'dout1']:
            fields[key] = 0 if value == 'off' else 1
        elif key in ['adc1', 'adc2']:
            raw_data['tags'].update({ "adc": key, })
            
            adc_fields = {}
            for adc_field, adc_value in value.items():
                adc_fields[adc_field] = float(adc_value)
            
            json_body.append({
                **raw_data,
                "fields": adc_fields
            })
        elif key in ['chn25', 'chn26']:
            fields.update({key: value})
        else:
            fields.update({key: float(value)})
    
    if fields:
        json_body.append({
            **raw_data,
            "fields": fields
        })
    
    return json_body

def iot_core_clean_data(message):
    clean_data = []

    result = message.get('result')
    sensorMessages = result.get('sensorMessages')
    if result and sensorMessages:
        for row in sensorMessages:

            raw_fields = row.get('plotLabels', '').split('|')
            raw_values = [float(i) for i in row.get('plotValues', '').split('|')]
            fields = dict(zip(raw_fields, raw_values))

            raw_data = {
                "measurement": row.get('applicationID'),
                "tags": {
                    "sensorID": row.get('sensorID'),
                    "sensorName": row.get('sensorName'),
                },
                "fields": fields
            }
            clean_data.append(raw_data)

    return clean_data
