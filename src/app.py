from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def homePage():
    return render_template("login.html")

@app.route("/predict", methods = ['GET', 'POST'])
def predictPage():
    return render_template("predict.html")

@app.route("/submit",  methods = ['GET', 'POST'])
def predict():
    cur_time = request.form['cur_time']
    cur_loc = request.form['cur_loc']
    exp_time = request.form['exp_time']
    
    con = sqlite3.connect('../bin/historicalData.db')
    c = con.cursor()

    sql = f"SELECT time, COUNT(time) AS max_time FROM (SELECT * FROM history WHERE location = '{cur_loc}') GROUP BY location ORDER BY max_time DESC LIMIT 1"
    for ele in c.execute(sql):
        hist_time = ele[0]

    hist_hh, hist_mm = int(hist_time.split(':')[0]), int(hist_time.split(':')[1])
    hist_time = hist_hh * 60 + hist_mm

    cur_hh, cur_mm = int(cur_time.split(':')[0]), int(cur_time.split(':')[1])
    cur_time = cur_hh * 60 + cur_mm

    diff = abs(hist_time - cur_time)

    hours = diff / 60
    minutes = diff % 60

    exp_hh, exp_mm = int(exp_time.split(':')[0]) + hours, int(exp_time.split(':')[1]) + minutes

    if exp_mm >= 60:
        exp_mm = exp_mm % 60
        exp_hh += exp_mm / 60

    exp_time = str("%d:%02d"%(exp_hh,exp_mm))
    #print(f"Expected time : {exp_time}")

    sql = f"SELECT location, COUNT(location) AS max_loc FROM (SELECT * FROM history WHERE time = '{exp_time}') GROUP BY location ORDER BY max_loc DESC LIMIT 1"
    for ele in c.execute(sql):
        predict_loc = ele[0]

    con.commit()
    con.close()

    #print(f"Prediction : {predict_loc}")
    return render_template("predict.html", prediction = predict_loc)

if __name__ == "__main__":
    app.run(debug=True)