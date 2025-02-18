from flask import Flask, request, render_template
from BackEnd import BkE
app = Flask("__name__")

@app.route('/')
def renderThisPath():
    res = render_template('template-file.html')
    return res

@app.route('/submit', methods=['POST'])
def submit():
    age = request.form['age']
    alcohol = request.form['alcohol']
    diet = request.form['diet']
    phys_act = request.form['phys_act']
    smoking = request.form['smoking']
    gender = request.form['gender']
    lastAppoint = request.form['lastAppoint']

    return render_template('response.html',Response = BkE.prognosis(age,alcohol,diet,phys_act,smoking,gender,lastAppoint))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)