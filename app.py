
from flask import Flask,render_template,request,redirect
from flask_cors import CORS
import joblib

app=Flask(__name__)
CORS(app)



@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/analyse/',methods=['POST'])
def analyse():
    plasma=request.form['plasma']
    bmi = request.form['bmi']
    age=request.form['age']
    np=request.form['preg']
    data=[[plasma,bmi,age,np]]


    res=predict(data)

    return render_template('/result.html',value=res)


def predict(data):
    model=joblib.load('model/Diab_Pred.sav')
    db_map={0:'NON-DIABETIC',1:'DIABETIC'}
    pred=model.predict(data)[0]
    res=db_map.get(pred)
    return res



if __name__ == '__main__':
    app.run()