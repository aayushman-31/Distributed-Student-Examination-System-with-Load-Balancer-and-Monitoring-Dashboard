from flask import Flask,request,jsonify
import sqlite3

app=Flask(__name__)

q=[
{"q":"Capital of India","o":["Delhi","Mumbai","Kolkata","Chennai"],"a":"Delhi"},
{"q":"5+5","o":["8","9","10","11"],"a":"10"},
{"q":"Sun rises from","o":["East","West","North","South"],"a":"East"},
{"q":"2*6","o":["10","11","12","13"],"a":"12"},
{"q":"Water formula","o":["H2O","CO2","O2","NaCl"],"a":"H2O"},
{"q":"Largest planet","o":["Mars","Earth","Jupiter","Venus"],"a":"Jupiter"},
{"q":"3+7","o":["8","9","10","11"],"a":"10"},
{"q":"Square root of 16","o":["2","3","4","5"],"a":"4"},
{"q":"Color of sky","o":["Blue","Red","Green","Black"],"a":"Blue"},
{"q":"10/2","o":["3","4","5","6"],"a":"5"}
]

@app.route("/exam")
def exam():
    return jsonify(q)

@app.route("/submit",methods=["POST"])
def submit():
    d=request.json
    ans=d["answers"]
    user=d["user"]
    s=0
    for i,a in enumerate(ans):
        if a==q[i]["a"]:
            s+=1
    con=sqlite3.connect("exam.db")
    c=con.cursor()
    c.execute("INSERT INTO scores VALUES(?,?)",(user,s))
    con.commit()
    con.close()
    return jsonify({"score":s})

app.run(host="0.0.0.0",port=5002)