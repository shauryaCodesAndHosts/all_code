from flask import request
from .database import db
from .models import History
from flask import current_app as app
import time
from flask import jsonify
def evaluate(exp):
    ans = 0
    vals = exp.split('/')
    print(vals)
    for x in range(0,len(vals)):
        if vals[x].isdigit():
            vals[x] = vals[x]
        else:
            if vals[x] == "minus":
                #print('found')
                vals[x] = '-'
            elif vals[x] == "plus":
                vals[x] = '+'
            elif vals[x] == "into":
                vals[x] = '*'
            elif vals[x] == "by":
                vals[x] = '/'
            else:
                return "wrong input" , "wrong input"
    print(vals)
    str_exp = ''
    for x in vals:
        str_exp = str_exp + x
    print(str_exp)
    try: 
        ans = eval(str_exp)
        new_entry = History(mathString = str_exp, timeOfEntry = time.time())
        db.session.add(new_entry)
        db.session.commit()
        #return ans
    except:
        ans = "Wrong input"
        str_exp = "Wrong input"
    return ans,str_exp

@app.route('/<path:exp>',methods=['GET','POST'])
def evalu(exp):
    print(exp)
    ans, ques = evaluate(exp)
    dic= {'question': ques, 'answer': ans}
    return jsonify(dic)

@app.route('/history',methods=['GET',"POST"])
def history():
    print('hisory')
    lastTwentyEntries = History.query.order_by(History.timeOfEntry.desc()).limit(20).all()
    print(lastTwentyEntries)
    ls = []
    for e in lastTwentyEntries:
        ls.append(e.serialize())
    return jsonify(ls)