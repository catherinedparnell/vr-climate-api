from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, this is my api'


# CSV:
# 1. temperature
# 2. precipitation
# 3. sea-level

# load in csv as pandas dataframe

# tags that correspond to SSP

# df[0][year] -> would give us theoretically the mean temperature

# return jsonify({ temp: temp, precip: precip, sealevel: sealevel })