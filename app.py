from flask import Flask, request, jsonify
import numpy as np
import pickle
app = Flask(__name__)

@app.route("/")
def home():
    return ("Hello world")
model = pickle.load(open("model.pkl", "rb"))



@app.route("/predict", methods=["GET", "POST"])
def predict():
    AGE = request.form.get('AGE')
    BP = request.form.get('BP')
    SG = request.form.get('SG')
    Albumin = request.form.get('Albumin')
    Sugar = request.form.get('Sugar')
    BGR = request.form.get('BGR')
    BloodUrea = request.form.get('BloodUrea')
    SerumCreatinine = request.form.get('SerumCreatinine')
    Sodium = request.form.get('Sodium')
    Potassium = request.form.get('Potassium')
    Hemoglobin = request.form.get('Hemoglobin')
    PackedCellVolume = request.form.get('PackedCellVolume')
    WBC = request.form.get('WBC')
    RBC = request.form.get('RBC')
    RedBloodCells = request.form.get('RedBloodCells')
    PusCells = request.form.get('PusCells')
    PusCellClumps = request.form.get('PusCellClumps')
    Bacteria = request.form.get('Bacteria')
    Hypertension = request.form.get('Hypertension')
    DiabetesMellitus = request.form.get('DiabetesMellitus')
    CAD = request.form.get('CAD')
    Appetite = request.form.get('Appetite')
    PedalEdema = request.form.get('PedalEdema')
    Anemia = request.form.get('Anemia')
    input_query = np.array([[AGE, BP, SG, Albumin, Sugar, BGR, BloodUrea, SerumCreatinine, Sodium, Potassium, Hemoglobin, PackedCellVolume, WBC, RBC, RedBloodCells, PusCells, PusCellClumps, Bacteria, Hypertension, DiabetesMellitus, CAD, Appetite, PedalEdema, Anemia]])
    result = model.predict(input_query)[0]
    return jsonify({'Chronic kidney Disease': str(result)})
    if __name__ == '__main__':
        app.run(debug=True)

    print(input_query)

    result = model.predict(sc.transform(input_query))
    print(result)
    return jsonify({'placement': str(result)})
if __name__ == '__main__':
    app.run(debug=True)






