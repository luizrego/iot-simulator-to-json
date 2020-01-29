import configparser
import json
import os
import random
import time
import datetime


def iot_simulator(val_serial_nr):
    list_values_front = []
    list_values_rear = []
    # set variables
    TEMPERATURE = 20
    HUMIDITY = 60
    i = 1

    while i < 11:
        curr_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = TEMPERATURE + (random.random() * 15)
        humidity = HUMIDITY + (random.random() * 20)
        dict_item_front = {"time": curr_datetime, "temperature": temperature, "humidity": humidity}
        dict_item_rear = {"time": curr_datetime, "temperature": temperature, "humidity": humidity} 
        list_values_front.append(dict_item_front)
        list_values_rear.append(dict_item_rear)
        i += 1
        time.sleep(1)

    data_dct = {"serial_number": val_serial_nr,"sensor_details": [{"front_sensor": {"sensor_id": "FW909301", "last_rev": datetime.datetime(2020, 1, 18).strftime("%Y-%m-%d"), "data": list_values_front}},
    {"rear_sensor": {"sensor_id": "FW909302", "last_rev": datetime.datetime(2020, 1, 14).strftime("%Y-%m-%d"), "data": list_values_rear}}]}
    
    return data_dct


def create_json_file(path_dir,val_serial_nr):
    try:
        input_json = iot_simulator(val_serial_nr) 
        json_file_name = 'data_{serial_nr}_{time}.json'.format(serial_nr = val_serial_nr, time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
        with open(path_dir+json_file_name, 'w+', encoding='utf-8') as f:
            json.dump(input_json, f, ensure_ascii=False, indent=4)
    except KeyboardInterrupt:
        print("process interrupted")


if __name__ == '__main__':

    config = configparser.ConfigParser()
    config.read('param.ini')
    output_dir = config['working_directory']['Output']

    print ( "IoT - Simulated device" )
    j = 0
    while j < 20: 
        create_json_file(output_dir,'TY7894020492')
        time.sleep(5)
        j += 1