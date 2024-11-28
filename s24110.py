from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = pd.DataFrame([request.json])
        else:
            data = pd.read_csv(request.files['file'])

        print(data.info())
        print(data.describe())
        data = pd.get_dummies(data, drop_first=True)
        print(data.info())
        print(data.describe())
        print('after',data)

        x_scaled = StandardScaler().fit_transform(data)

        print('more',x_scaled)

        prediction = model.predict(x_scaled)

        return jsonify({"prediction": prediction[0]})

    except Exception as e:
        return jsonify({"exception": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)