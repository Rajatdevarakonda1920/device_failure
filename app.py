from flask import Flask,render_template,request
import joblib

#intiliaze the app
app = Flask(__name__)
model = joblib.load(r'device_fail.pkl')
print('[INFO] model loaded')

#__name__ refers that this file main file in the module

@app.route('/')
def hello_world():
    return render_template('welcome.html')

@app.route('/predict' , methods = ['post'])
def predict():
    setting1 = request.form.get('setting1')
    setting2 = request.form.get('setting2')
    s1 = request.form.get('s1')
    s2 = request.form.get('s2')
    s3 = request.form.get('s3')
    s4 = request.form.get('s4')
    s5 = request.form.get('s5')
    s6 = request.form.get('s6')
    s7 = request.form.get('s7')
    s8 = request.form.get('s8')
    s9 = request.form.get('s9')
    s10 = request.form.get('s10')
    s11 = request.form.get('s11')
    s12 = request.form.get('s12')
    s13 = request.form.get('s13')
    s14 = request.form.get('s14')
    s15 = request.form.get('s15')
    s16 = request.form.get('s16')
    s17 = request.form.get('s17')
    s20 = request.form.get('s20')
    s21 = request.form.get('s21')

    output = model.predict([[setting1,setting2,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s20,s21]])
    if output[0]==1:
        print('Device Fail')
        result = 'Device Fail'
    else:
        print('Device Working')
        result = 'Device Working'
    return render_template('predict.html',predict=f'Your Results are {result}')

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,port=8080)



