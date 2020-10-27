
from flask import Blueprint, render_template
from flask import Flask, request, jsonify, Blueprint
import os
import pickle
import traceback
import pandas as pd
import numpy as np
import category_encoders

def load_model():
    print("LOADING THE MODEL...")
    with open(MODEL_FILEPATH, "rb") as model_file:
        saved_model = pickle.load(model_file)
    return saved_model

# Specify the filepath
MODEL_FILEPATH = os.path.join(os.path.dirname(__file__),"..","..", "model", "model.p")
lr = load_model()

home_routes = Blueprint("home_routes", __name__)

# Web app home route
@home_routes.route("/")
def index():
    area = ['Asia', 'Africa', 'America']
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return render_template("prediction_form.html", area=area, month=month)

# Predict route - called via API 
@home_routes.route('/predict', methods=['POST'])
def predict_json():
    if lr:
        try:
            json_ = request.json
            print(json_)            
            query = pd.DataFrame(json_)
            query_dict = query.to_dict()
            prediction = list(lr.predict(query))
            prediction_proba = list(lr.predict_proba(query))
            # breakpoint()
            #TODO: set correct datatypes and validate datatypes
            return jsonify(features = query_dict, prediction = str(prediction), prediction_proba=prediction_proba[0][1])
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Train the model first')
        return ('No model here to use')

# Predict route - called via web-app
@home_routes.route("/predict_form", methods=["POST"])
def predict_html():
    area = request.form["area"]
    month = request.form["month"]
    distance_from_port = float(request.form["distance_from_port"])
    speed = float(request.form["speed"])
    lat = float(request.form["lat"])
    lon = float(request.form["lon"])
    column_names = ["distance_from_port","speed","lat","lon","month", "area"]
    df_row = pd.DataFrame(columns = column_names)
    # df_row.append([[category,staff_pick,description_leng,usd_goal,cam_length]])
    df_row = df_row.append({'distance_from_port':distance_from_port,'speed':speed,'lat':lat,'lon':lon,'month':month,'area':area},ignore_index=True)
    df_row_dict = df_row.to_dict()
    #TODO: form design slider shows values for
    prediction = list(lr.predict(df_row))
    prediction_proba = list(lr.predict_proba(df_row))
    prediction_text = "Fishing" if prediction[0] == 1 else "Not Fishing"
    print(jsonify(prediction = str(prediction), prediction_proba=prediction_proba[0][1]))
    # return jsonify(features = df_row_dict, prediction = str(prediction), prediction_proba=prediction_proba[0][1])
    return render_template("prediction_results.html", features = df_row_dict, prediction = str(prediction_text), prediction_proba=prediction_proba[0][1])

    #TODO: exception handling like for predict_json
    # TODO: should this be consolidted with the predict_json route?



