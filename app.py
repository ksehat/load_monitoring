from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

data = {"flight_num":45687,"FlightRoute":"MHD>THR","data":{"0":{"date":"2023-01-10","actual":78.5,"pred":77.36},"1":{"date":"2023-01-11","actual":78.5,"pred":77.36},"2":{"date":"2023-01-12","actual":78.5,"pred":77.36}}}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    flight_num = request.args.get('flight_num')
    flight_route = request.args.get('flight_route')

    # Use the flight_num and flight_route to get the corresponding data
    # For example:
    data = get_data_from_api(flight_num, flight_route)

    return jsonify(data)


def get_data_from_api(flight_num, flight_route):
    data = json.loads(requests.post().content)

if __name__ == '__main__':
    app.run()