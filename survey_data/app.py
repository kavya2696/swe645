#1. Kavya Shivakumar (G01520934)
#2. Sehaj Gill (G01535820)
#3. Jaanaki Swaroop P(G01502869)
#4. Koushik Vasa (G01480627)

from flask import Flask, request, Response
from flask_sqlalchemy import SQLAlchemy
from collections import OrderedDict
import json

app = Flask(__name__)

# Replace with your Amazon RDS MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://admin:swaroopp@database-2.c3h9lfniyvdb.us-east-1.rds.amazonaws.com/exd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Defining the Survey
class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    zip = db.Column(db.String(20), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    survey_date = db.Column(db.String(20), nullable=False)
    likings = db.Column(db.String(255), nullable=True)
    interest = db.Column(db.String(50), nullable=False)
    recommendation = db.Column(db.String(50), nullable=True)
    comments = db.Column(db.String(255), nullable=True)

    # Converting object to dictionary
    def to_dict(self):
        return OrderedDict([
            ("first_name", self.first_name),
            ("last_name", self.last_name),
            ("address", self.address),
            ("city", self.city),
            ("state", self.state),
            ("zip", self.zip),
            ("telephone", self.telephone),
            ("email", self.email),
            ("survey_date", self.survey_date),
            ("likings", self.likings),
            ("interest", self.interest),
            ("recommendation", self.recommendation),
            ("comments", self.comments)
        ])

#to create new survey
@app.route('/survey', methods=['POST'])
def create_survey():
    data = request.json
    survey = Survey(
        first_name=data['first_name'],
        last_name=data['last_name'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        zip=data['zip'],
        telephone=data['telephone'],
        email=data['email'],
        survey_date=data['survey_date'],
        likings=data.get('likings'),
        interest=data['interest'],
        recommendation=data.get('recommendation'),
        comments=data.get('comments')
    )
    db.session.add(survey)
    db.session.commit()
    return Response(json.dumps({
        'message': 'Survey created',
        'survey': survey.to_dict()
    }), mimetype='application/json', status=201)

#to retrieve survey
@app.route('/survey', methods=['GET'])
def get_all_surveys():
    surveys = Survey.query.all()
    ordered_data = [s.to_dict() for s in surveys]
    return Response(json.dumps(ordered_data), mimetype='application/json')

#to retrieve by specific survey by ID
@app.route('/survey/<int:id>', methods=['GET'])
def get_survey(id):
    survey = Survey.query.get_or_404(id)
    return Response(json.dumps(survey.to_dict()), mimetype='application/json')

#to update the existing survey
@app.route('/survey/<int:id>', methods=['PUT'])
def update_survey(id):
    data = request.json
    survey = Survey.query.get_or_404(id)
    for key in data:
        if hasattr(survey, key):
            setattr(survey, key, data[key])
    db.session.commit()
    return Response(json.dumps({
        'message': 'Survey updated',
        'survey': survey.to_dict()
    }), mimetype='application/json')

#to delete the survey
@app.route('/survey/<int:id>', methods=['DELETE'])
def delete_survey(id):
    survey = Survey.query.get_or_404(id)
    db.session.delete(survey)
    db.session.commit()
    return Response(json.dumps({'message': 'Survey deleted'}), mimetype='application/json')

if __name__ == '__main__':
    #to run the app
    app.run(host='0.0.0.0', port=5000, debug=True)

