
from flask import Flask, request, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Simulated database (in-memory)
data_storage = {
    "physical_activity": [],
    "sleep_patterns": []
}

@app.route('/upload/physical_activity', methods=['POST'])
def upload_physical_activity():
    """Endpoint for uploading physical activity data."""
    data = request.json
    data_storage["physical_activity"].append(data)
    return jsonify({"message": "Physical activity data uploaded successfully"}), 200

@app.route('/upload/sleep_patterns', methods=['POST'])
def upload_sleep_patterns():
    """Endpoint for uploading sleep pattern data."""
    data = request.json
    data_storage["sleep_patterns"].append(data)
    return jsonify({"message": "Sleep pattern data uploaded successfully"}), 200

@app.route('/analyze/sleep_quality', methods=['GET'])
def analyze_sleep_quality():
    """Endpoint to analyze and return sleep quality information."""
    sleep_data = pd.DataFrame(data_storage["sleep_patterns"])
    # Example analysis: Calculate average sleep duration
    sleep_data['start'] = pd.to_datetime(sleep_data['start'])
    sleep_data['end'] = pd.to_datetime(sleep_data['end'])
    sleep_data['duration'] = sleep_data['end'] - sleep_data['start']
    average_sleep_duration = sleep_data['duration'].mean()
    return jsonify({"average_sleep_duration": str(average_sleep_duration)}), 200

if __name__ == '__main__':
    app.run(debug=True)



#Example provided by client:

# {
#   "date": "2024-04-01",
#   "steps": 10000,
#   "calories_burned": 500
# }


# {
#   "date": "2024-04-01",
#   "start": "2024-04-01T22:00:00",
#   "end": "2024-04-02T07:00:00"
# }
