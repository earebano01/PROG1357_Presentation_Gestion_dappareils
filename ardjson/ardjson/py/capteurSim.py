import requests
import random
import time
from datetime import datetime, timedelta

API_ENDPOINT = "http://192.168.5.198:8080/api/data"
DHT_PIN = 4

def generate_random_values(sensor_type):
    if sensor_type == "temperature":
        return round(random.uniform(20, 30), 2)  # Température aléatoire entre 20°C et 30°C, arrondie à 2 décimales
    elif sensor_type == "humidity":
        return round(random.uniform(40, 60), 2)  # Humidité aléatoire entre 40% et 60%, arrondie à 2 décimales
    elif sensor_type == "sound":
        return random.randint(800, 1200)  # Valeur sonore aléatoire entre 800 et 1200
    elif sensor_type == "photoresistor":
        return random.randint(500, 1000)  # Valeur de photoresistor aléatoire entre 500 et 1000

def get_current_date():
    return datetime.now().strftime('%Y-%m-%d')

def get_current_time():
    current_time = datetime.now() - timedelta(hours=3)  
    return current_time.strftime('%H:%M')

def send_data(deviceid, data, date, time, room):
    data["deviceid"] = deviceid
    data["date"] = date
    data["time"] = time
    data["room"] = room  # Ajout du champ "room" avec le numéro de chambre spécifié
    try:
        response = requests.post(API_ENDPOINT, json=data)
        if response.status_code == 200:
            print(data)
        else:
            print(f"Échec de l'envoi des données. Code de statut : {response.status_code}")
    except Exception as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    interval_seconds = 5

    while True:
        try:
            # Chambre 100
            room = 100
            # Capteur de température et d'humidité
            deviceid = "ca492093a449d75d"
            temperature = generate_random_values("temperature")
            humidity = generate_random_values("humidity")
            date = get_current_date()
            time_now = get_current_time()
            send_data(deviceid, {"temperature": temperature, "humidity": humidity}, date, time_now, room)

            # Capteur de son
            deviceid = "fa81efab546fde6e"
            sound = generate_random_values("sound")
            send_data(deviceid, {"sound": sound}, date, time_now, room)

            # Capteur de photoresistor
            deviceid = "ce25e9768cfe0061"
            photoresistor = generate_random_values("photoresistor")
            relay_state = "on" if photoresistor > 750 else "off"  # Supposons que le relais est allumé si le photoresistor > 750
            send_data(deviceid, {"photoresistor": photoresistor, "relay": relay_state}, date, time_now, room)


            # Chambre 101
            room = 101
            # Capteur de température et d'humidité
            deviceid = "e679ffef482bdf83"
            temperature = generate_random_values("temperature")
            humidity = generate_random_values("humidity")
            date = get_current_date()
            time_now = get_current_time()
            send_data(deviceid, {"temperature": temperature, "humidity": humidity}, date, time_now, room)

            # Capteur de son
            deviceid = "c6246ed1e7818f38"
            sound = generate_random_values("sound")
            send_data(deviceid, {"sound": sound}, date, time_now, room)

            # Capteur de photoresistor
            deviceid = "36aba54e530c62e4"
            photoresistor = generate_random_values("photoresistor")
            relay_state = "on" if photoresistor > 750 else "off"  # Supposons que le relais est allumé si le photoresistor > 750
            send_data(deviceid, {"photoresistor": photoresistor, "relay": relay_state}, date, time_now, room)

            # Chambre 102
            room = 102
            # Capteur de température et d'humidité
            deviceid = "b208562920606844"
            temperature = generate_random_values("temperature")
            humidity = generate_random_values("humidity")
            send_data(deviceid, {"temperature": temperature, "humidity": humidity}, date, time_now, room)

            # Capteur de son
            deviceid = "be701dab163bc0a0"
            sound = generate_random_values("sound")
            send_data(deviceid, {"sound": sound}, date, time_now, room)

            # Capteur de photoresistor
            deviceid = "d64f76c7075a3eac"
            photoresistor = generate_random_values("photoresistor")
            relay_state = "on" if photoresistor > 750 else "off"  # Supposons que le relais est allumé si le photoresistor > 750
            send_data(deviceid, {"photoresistor": photoresistor, "relay": relay_state}, date, time_now, room)

            # Chambre 103
            room = 103
            # Capteur de température et d'humidité
            deviceid = "ea3359fe03c4afca"
            temperature = generate_random_values("temperature")
            humidity = generate_random_values("humidity")
            send_data(deviceid, {"temperature": temperature, "humidity": humidity}, date, time_now, room)

            # Capteur de son
            deviceid = "f2512ea544d2eafc"
            sound = generate_random_values("sound")
            send_data(deviceid, {"sound": sound}, date, time_now, room)

            # Capteur de photoresistor
            deviceid = "da8168b3804c3012"
            photoresistor = generate_random_values("photoresistor")
            relay_state = "on" if photoresistor > 750 else "off"  # Supposons que le relais est allumé si le photoresistor > 750
            send_data(deviceid, {"photoresistor": photoresistor, "relay": relay_state}, date, time_now, room)

        except Exception as e:
            print(f"Erreur : {e}")

        time.sleep(interval_seconds)
