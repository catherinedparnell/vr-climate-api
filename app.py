from flask import Flask, jsonify, request
import methods as METHODS
import constants as CONSTANTS
import processing as PROCESSING

app = Flask(__name__)

@app.route('/')
def get_data():
    dfs = METHODS.make_dfs()

    year = request.args.get('year', type=int)
    scenario_input = request.args.get('scenario', type=int)

    if scenario_input == 0:
        scenario = CONSTANTS.SCENARIO_A
    elif scenario_input == 1:
        scenario = CONSTANTS.SCENARIO_B
    elif scenario_input == 2:
        scenario = CONSTANTS.SCENARIO_C
    else:
        scenario = -1

    if (scenario == -1):
        return 'There was an error in your scenario input'

    precip = METHODS.get_precip(dfs, year, scenario)
    temp = METHODS.get_temp(dfs, year, scenario)
    sea_level = METHODS.get_sea_level(dfs, year, scenario)

    res = {
        "precip": PROCESSING.processPrecip(precip),
        "temperature": {
            "celsius": temp,
            "fahrenheit": PROCESSING.processTemp(temp)
        },
        "sea_level": sea_level
    }
    
    return jsonify(res)

@app.route('/decade')
def get_data_by_decade():
    dfs = METHODS.make_dfs()

    year = request.args.get('year', type=int)
    scenario_input = request.args.get('scenario', type=int)

    if scenario_input == 0:
        scenario = CONSTANTS.SCENARIO_A
    elif scenario_input == 1:
        scenario = CONSTANTS.SCENARIO_B
    elif scenario_input == 2:
        scenario = CONSTANTS.SCENARIO_C
    else:
        scenario = -1

    if (scenario == -1):
        return 'There was an error in your scenario input'

    precip = METHODS.accumulate_decade(dfs, year, scenario, METHODS.get_precip)
    temp = METHODS.accumulate_decade(dfs, year, scenario, METHODS.get_temp)
    sea_level = METHODS.accumulate_decade(dfs, year, scenario, METHODS.get_sea_level)

    res = {
        "precip": PROCESSING.processPrecip(precip),
        "temperature": {
            "celsius": temp,
            "fahrenheit": PROCESSING.processTemp(temp)
        },
        "sea_level": sea_level
    }
    
    return jsonify(res)