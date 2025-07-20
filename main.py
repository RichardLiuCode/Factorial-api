import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from process import calculate
import math

app = Flask(__name__)
CORS(app)


def isNan(n):
  try:
    if math.isnan(float(n)):
      return True
    else:
      return False
  except ValueError:
      return True

@app.route('/')
def index():
  return '<h1>Factorial api</h1><br><p>Try calc?q=3</p>'


@app.route('/calc', methods=['GET'])
def get():
  inputParams = request.args.get('q')
  if inputParams == "":
    return jsonify({"error": "No input! Please provide a number", "result": "--"}),400
  elif isNan(inputParams):
    return jsonify({"error": "Input is not a number", "result": "--"}),400
  elif int(inputParams) < 1:
    print("error the input is 0 or a nagative number.")
    return jsonify({"error": "Input must be larger than 1", "result": "--"}),400
  else:
    print("input: ", inputParams)
    output = calculate(inputParams)
    return jsonify({"input": inputParams, "result": output,"error":False})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
app.run(host='0.0.0.0', port=8080)

