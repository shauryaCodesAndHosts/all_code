from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
#import os
#from flask_sqlalchemy import SQLAlchemy
#current_dir= os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    print("hello")
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        plantName = request.form["plantName"]
        areaName = request.form["areaName"]
        partType = request.form["partType"]
        partName = request.form["partName"]
        partUniqueNumber = request.form["partUniqueNumber"]
        calibrationCode = request.form["calibrationCode"]
        reminderInDays = request.form["reminderInDays"]
        remarks = request.form['remarks']
        ls = [plantName, areaName, partType, partName, partUniqueNumber,calibrationCode, reminderInDays, remarks ]
        print(ls)
        #add_data(ls)
        return render_template('index.html')
    

@app.route('/get_options/<selected_option>', methods=['GET'])
def get_options(selected_option):
    # Fetch options based on the selected_option from the dictionary
    plantAnd_Area = {
        'Pune':['Paint Shop','Rear Axle', 'Front Axle', 'Trim 1', 'Trim 2', 'Trim 3', 'TCF 1', 'TCF 2', 'TCF 3', 'TIW', 'IBF'],
        'Jamshedpur':['Paint Shop','Rear Axle', 'Front Axle', 'Trim 1', 'Trim 2', 'Trim 3', 'TCF 1', 'TCF 2', 'TCF 3', 'TIW', 'IBF'],
        'Lucknow':['Paint Shop','Rear Axle', 'Front Axle', 'Trim 1', 'Trim 2', 'TCF 1', 'TCF 2', 'TIW', 'IBF'],
        'Dharwad':['Rear Axle', 'Front Axle', 'Trim 1', 'Trim 2', 'TCF 1', 'TCF 2', 'TIW', 'IBF'],
    }
    options = plantAnd_Area.get(selected_option)
    print(selected_option)
    print(options)
    return jsonify(options)

if __name__ == "__main__":
    app.run(debug=True )
