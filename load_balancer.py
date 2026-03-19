from flask import Flask,request,jsonify,render_template
import requests
import threading
import time
from datetime import datetime

app=Flask(__name__)

servers=[
"http://192.168.2.207:5001",
"http://192.168.2.207:5002"
]

status={s:"DOWN" for s in servers}
history=[]

i=0
last="None"

def next_server():
    global i
    s=servers[i]
    i=(i+1)%len(servers)
    return s

def health_check():
    while True:
        for s in servers:
            try:
                requests.get(s+"/exam",timeout=1)
                status[s]="UP"
            except:
                status[s]="DOWN"
        time.sleep(2)

threading.Thread(target=health_check,daemon=True).start()

def log(user,server,endpoint):
    history.append({
        "user":user,
        "server":server,
        "endpoint":endpoint,
        "time":datetime.now().strftime("%H:%M:%S")
    })

@app.route("/exam")
def exam():
    global last
    user=request.args.get("user","unknown")
    for _ in range(len(servers)):
        s=next_server()
        if status[s]=="UP":
            try:
                r=requests.get(s+"/exam")
                last=s
                log(user,s,"/exam")
                return jsonify(r.json())
            except:
                continue
    return {"error":"servers down"}

@app.route("/submit",methods=["POST"])
def submit():
    global last
    d=request.json
    user=d.get("user","unknown")
    for _ in range(len(servers)):
        s=next_server()
        if status[s]=="UP":
            try:
                r=requests.post(s+"/submit",json=d)
                last=s
                log(user,s,"/submit")
                return jsonify(r.json())
            except:
                continue
    return {"error":"servers down"}

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html",status=status,last=last,history=history[::-1])

app.run(host="0.0.0.0",port=8000)