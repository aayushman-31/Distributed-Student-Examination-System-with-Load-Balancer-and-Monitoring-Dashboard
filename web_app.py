from flask import Flask,request,redirect,render_template
import requests
import sqlite3

app=Flask(__name__)

LB = "http://192.168.2.207:8000"

user=""

@app.route("/",methods=["GET","POST"])
def login():
    global user
    if request.method=="POST":
        u=request.form["u"]
        p=request.form["p"]
        con=sqlite3.connect("exam.db")
        c=con.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?",(u,p))
        r=c.fetchone()
        con.close()
        if r:
            user=u
            return redirect("/exam")
    return render_template("login.html")

@app.route("/exam")
def exam():
    r=requests.get(LB+"/exam",params={"user":user})
    q=r.json()
    return render_template("exam.html",questions=q)

@app.route("/submit",methods=["POST"])
def submit():
    a=[]
    for i in range(10):
        a.append(request.form.get(str(i)))
    r=requests.post(LB+"/submit",json={"answers":a,"user":user})
    s=r.json()["score"]
    return render_template("result.html",score=s)

app.run(host="0.0.0.0",port=5000)