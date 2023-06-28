def clean_data(app_list, message):
    data_list = []
    topic = message.get('topic')
    result = message.get('result')
    keys_list = ['humidity', 'temperature', 'water_leak', 'adc1', 'adc2']

    if topic in app_list and result:
        if result.get('object'):
            # print(result.get('object'))
            for key, value in result['object'].items():
                if key in keys_list:
                    print(f"{topic} >>> object : {result.get('object')}")
                    break