from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db = SQLAlchemy(app)

class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    visits = db.relationship('Visit', backref='doctor', cascade="all, delete")


class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    visits = db.relationship('Visit', backref='patient', cascade="all, delete")


class Visit(db.Model):
    __tablename__ = 'visits'
    id = db.Column(db.Integer, primary_key=True)

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id', ondelete='CASCADE'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id', ondelete='CASCADE'))

    date = db.Column(db.String(20))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


menga shunaqa 100 foiz toliq qilib 5 ta masala yozib ber
