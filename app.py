from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///attend.db"
app.config['SQLALCHEMY_DATABASE_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class attend(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    present = db.Column(db.Integer, nullable = False)
    absent = db.Column(db.Integer, nullable = False)
    percent = db.Column(db.Integer, nullable = False)
    def _repr_(self) -> str:
        return f"{self.sno} - {self.name} - {self.present} - {self.absent} - {self.percent}"
    
@app.route("/", methods = ['GET', 'POST'])
def per():
    if(request.method == 'POST'):
        NAME = request.form['name']
        PRESENT = int(request.form['present'])
        ABSENT = 15-PRESENT
        PERCENT = (PRESENT/15)*100

        ATTEND = attend(name = NAME, present = PRESENT, absent = ABSENT, percent = PERCENT)
        db.session.add(ATTEND)
        db.session.commit()
        return redirect('/')

    return render_template('index.html')

@app.route('/summary')
def sum():
    alldata = attend.query.all()
    return render_template('summary.html', alldata = alldata)

if _name_ == "_main_":
    with app.app_context():
        db.create_all()
    app.run(debug = True)