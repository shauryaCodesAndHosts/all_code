from flask import Flask
from flask import jsonify
app = Flask(__name__)
app.app_context().push()

def reading_data(ls):
    with open('./last20.txt', "r") as file:
        for line in file:
            data = eval(line)
            latest.append(data)

latest = []
reading_data(latest)

@app.route('/<path:exp>',methods=['GET','POST'])
def calc(exp):
    ls = exp.split('/')
    s = ""
    for x in ls :
        if x == "minus":
            s = s+'-'
        elif x == "plus":
            s = s+'+'
        elif x == "into":
            s = s+'*'
        elif x == "by":
            s = s+'/'
        else:
            s=s+x
    n= eval(s)
    dic= {'question': s, 'answer': n}
    latest.insert(0,dic)
    c=0
    with open('./last20.txt', "w") as file:
        for item in latest:
            file.write(str(item) + "\n") 
            c=c+1
            if c>=20:
                break 
    return jsonify(dic)
@app.route('/history',methods=["GET"])
def history():
    lss =[]
    with open('./last20.txt', "r") as file:
        for line in file:
            data = eval(line)
            lss.append(data)
    return jsonify(lss)

if __name__ == "__main__":
    app.run(debug=True, port='2000')