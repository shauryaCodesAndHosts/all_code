from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
current_dir= os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(current_dir,'calibrationOfTools.sqlite3')
db=SQLAlchemy()
db.init_app(app)
app.app_context().push()


class Form(db.Model):
    __tablename__ = 'form_data'
    id = db.Column(db.Integer, autoincrement=True, primary_key= True,  nullable= False)
    plantName = db.Column(db.String )
    areaName = db.Column(db.String)
    partType = db.Column(db.String )
    partName = db.Column(db.String )
    partUniqueNumber = db.Column(db.String )
    calibarationDate = db.Column(db.String )
    nextCalibarationDate = db.Column(db.String)
    reminderInDays = db.Column(db.String )
    remarks = db.Column(db.String )
    dateOfEntry=db.Column(db.String)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        plantName = request.form["plantName"]
        areaName = request.form["areaName"]
        partType = request.form["partType"]
        partName = request.form["partName"]
        partUniqueNumber = request.form["partUniqueNumber"]
        calibarationDate = request.form["calibarationDate"]
        nextCalibarationDate = request.form['nextCalibarationDate']
        reminderInDays = request.form["reminderInDays"]
        remarks = request.form['remarks']
        ls = [plantName, areaName, partType, partName, partUniqueNumber,calibarationDate,nextCalibarationDate , reminderInDays, remarks ]
        print(ls)
        add_data(ls)

        return render_template('index.html')

def add_data(new_data):
    new_record= Form(plantName=new_data[0],
                     areaName=new_data[1],
                     partType = new_data[2],
                     partName= new_data[3],
                     partUniqueNumber= new_data[4],
                     calibarationDate = new_data[5],
                     nextCalibarationDate = new_data[6],
                     reminderInDays = int(new_data[7]),
                     remarks= new_data[8],
                     dateOfEntry=datetime.today()
                     )
    print(new_record)
    db.session.add(new_record)
    db.session.commit()

@app.route('/parts',methods=['GET','POST'])
def parts_display():
    all_parts = Form.query.all()
    updateRemainingDays()
    print(all_parts)
    return render_template('parts.html',forms=all_parts)

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
    #print(selected_option)
    #print(options)
    return jsonify(options)

@app.route('/parts/delete/<id>',methods=['GET'])
def deleteFormData(id):
    part=Form.query.filter_by(id=id).first()
    print(part)
    db.session.delete(part)
    db.session.commit()
    return redirect(url_for('parts_display'))

def updateRemainingDays():
    print(read_date()[0:10],str(datetime.now().date()))
    if read_date()[0:10] == str(datetime.now().date()):
        print(read_date()[0:10],str(datetime.now().date()))
        print('aaj ka din ')
    else:
        write_date()
        all_parts=Form.query.all()
        print('in update remaining days')
        last_update=read_date()
        for part in all_parts:
            if int(part.reminderInDays) > 0:
                part.reminderInDays=str(int(part.reminderInDays)-1)
            db.session.commit()

def read_date():
    file_path = 'date.txt'
    # Read the date from the text file
    with open(file_path, 'r') as file:
        date_string = file.read()
        file.close
    date_object = datetime.strptime(date_string.strip(), '%Y-%m-%d')
    return str(date_object)
    print(date_object)

def write_date():
    current_date = datetime.now()
    date_string = current_date.strftime('%Y-%m-%d')
    file_path = 'date.txt'
    with open(file_path, 'w') as file:
        file.write(date_string)
        file.close()


if __name__ == "__main__":
    app.run(debug=True, port='8081' )
    updateRemainingDays()