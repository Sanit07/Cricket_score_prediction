from flask import Flask,jsonify,render_template,request
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    temp=[]
    if request.method =='POST':
        runs=int(request.form['runs'])
        wickets=int(request.form['wickets'])
        overs=float(request.form['over'])
        runs_last_5=int(request.form['runs_last_5'])
        wickets_last_5=int(request.form['wickets_last_5'])
        temp=list(map(int,request.form['team_1'].strip()))
        temp=temp + list(map(int,request.form['team_2'].strip()))
        temp=[runs,wickets,overs,runs_last_5,wickets_last_5] + temp
        o=model.predict([temp])
        output=int(o[0])
        ll=output-10
        ul=output+10
        return render_template('result.html',prediction=f'The Prediction score is {ll} to {ul}')
    else:
        return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)