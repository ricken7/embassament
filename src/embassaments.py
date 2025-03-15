from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# URL base de la API
BASE_URL = "http://aca-web.gencat.cat/sdim2/apirest"

# Función para obtener la lista de sensores de embalses
def get_embassament_sensors():
    url = f"{BASE_URL}/catalog?componentType=embassament"
    try:
        response = requests.get(url, timeout=20)  # Timeout de 20 segundos
        response.raise_for_status()  # Lanza una excepción si la petición no fue exitosa
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching embassament sensors: {e}")
        return {}

# Función para obtener la última medida de un sensor específico
def get_last_measure(provider, sensor):
    url = f"{BASE_URL}/data/{provider}/{sensor}"
    try:
        response = requests.get(url, timeout=20)  # Timeout de 20 segundos
        response.raise_for_status()  # Lanza una excepción si la petición no fue exitosa
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching last measure for {provider}/{sensor}: {e}")
        return {}

# Función para procesar los datos de los sensores
def process_sensors_data():
    sensors_response = get_embassament_sensors()
    if "providers" in sensors_response:
        sensors_data = sensors_response["providers"]
    else:
        sensors_data = []
        print("No providers found in the response.")
    
    embassament_data = []
    for provider_data in sensors_data:
        provider = provider_data["provider"]
        for sensor in provider_data["sensors"]:
            if sensor["description"] == "Volum embassat":
                sensor_id = sensor["sensor"]
                component_desc = sensor["componentDesc"]
                capacitat_maxima = sensor["componentAdditionalInfo"].get("Capacitat màxima embassament", "N/A")
                
                # Obtener la última medida del sensor
                measure_data = get_last_measure(provider, sensor_id)
                if not measure_data:
                    continue  # Saltar si no se pudo obtener la medida
                
                last_measure = float(measure_data["observations"][0]["value"])
                timestamp = measure_data["observations"][0]["timestamp"]

                # Agregar los datos del embalse a la lista
                embassament_data.append({
                    "embassament": component_desc,
                    "capacitat_maxima": capacitat_maxima,
                    "volum_embassat_actual": last_measure,
                    "fecha_hora": timestamp
                })
    return embassament_data

# Función para calcular el porcentaje global y obtener la fecha más reciente
def calculate_global_percentage_and_newest_date():
    sensors_response = get_embassament_sensors()
    if "providers" in sensors_response:
        sensors_data = sensors_response["providers"]
    else:
        sensors_data = []
        print("No providers found in the response.")
    
    total_volum_embassat = 0
    total_capacitat_maxima = 0
    newest_date = None

    for provider_data in sensors_data:
        provider = provider_data["provider"]
        for sensor in provider_data["sensors"]:
            if sensor["description"] == "Volum embassat":
                sensor_id = sensor["sensor"]
                component_desc = sensor["componentDesc"]
                
                # Excluir el embassament Gaià (el Catllar)
                if component_desc == "Gaià (el Catllar)":
                    continue
                
                capacitat_maxima_str = sensor["componentAdditionalInfo"].get("Capacitat màxima embassament", "0").replace(" hm³", "").replace(",", ".")
                capacitat_maxima = float(capacitat_maxima_str)
                
                # Obtener la última medida del sensor
                measure_data = get_last_measure(provider, sensor_id)
                if not measure_data:
                    continue  # Saltar si no se pudo obtener la medida
                
                last_measure = float(measure_data["observations"][0]["value"])
                timestamp = measure_data["observations"][0]["timestamp"]
                
                # Sumar los valores
                total_volum_embassat += last_measure
                total_capacitat_maxima += capacitat_maxima

                # Actualizar la fecha más reciente
                if newest_date is None or timestamp > newest_date:
                    newest_date = timestamp

    if total_capacitat_maxima > 0:
        global_percentage = (total_volum_embassat / total_capacitat_maxima) * 100
    else:
        global_percentage = 0
    
    return global_percentage, newest_date

@app.route('/embassaments', methods=['GET'])
def embassaments():
    embassament_data = process_sensors_data()
    return jsonify(embassament_data)

@app.route('/global_percentage', methods=['GET'])
def global_percentage_route():
    global_percentage, newest_date = calculate_global_percentage_and_newest_date()
    return jsonify({"global_percentage": global_percentage, "newest_date": newest_date})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Iniciando servidor...")
    app.run(debug=False, host='0.0.0.0', port=port)

