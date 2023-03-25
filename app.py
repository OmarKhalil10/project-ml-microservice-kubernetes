from flask import Flask, request, jsonify
from flask.logging import create_logger
from flask_cors import CORS
import logging

import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from flask.templating import render_template

app = Flask(__name__)
cors = CORS(app)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

    LOG.info(f"Scaling Payload: \n{payload}")
    scaler = StandardScaler().fit(payload.astype(float))
    scaled_adhoc_predict = scaler.transform(payload.astype(float))
    return scaled_adhoc_predict

@app.route("/")
def home():
    # Uncomment the following line to display the simple HTML header for the home page
    # html = f"<h3>Sklearn Prediction Home</h3>"
    # return html.format(format)
    
    # Comment out the following line if you don't want to display the home page
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    """Performs an sklearn prediction

        input looks like:
        {
        "CHAS":{
        "0":0
        },
        "RM":{
        "0":6.575
        },
        "TAX":{
        "0":296.0
        },
        "PTRATIO":{
        "0":15.3
        },
        "B":{
        "0":396.9
        },
        "LSTAT":{
        "0":4.98
        }

        result looks like:
        { "prediction": [ <val> ] }

        """
    # Commet out the following line before deploying to production [Required Fix]
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    # Logging the input payload
    json_payload = request.json
    LOG.info(f"JSON payload: \n{json_payload}")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info(f"Inference payload DataFrame: \n{inference_payload}")
    # scale the input
    scaled_payload = scale(inference_payload)
    # get an output prediction from the pretrained model, clf
    prediction = list(clf.predict(scaled_payload))
    # TO DO:  Log the output prediction value
    LOG.info(f"output prediction: {prediction}")
    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    # load pretrained model as clf
    clf = joblib.load("./model_data/boston_housing_prediction.joblib")
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
