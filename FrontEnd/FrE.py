from flask import Flask, request, render_template


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

    return f"""
        Ηλικία: {age}<br>
        Αλκοόλ: {alcohol}<br>
        Δίαιτα: {diet}<br>
        Σωματική Δραστηριότητα: {phys_act}<br>
        Καπνίσμα: {smoking}<br>
        Φύλο: {gender}<br>
        Τελευταία Επίσκεψη: {lastAppoint}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)