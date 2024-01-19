import os

from flask import Flask, render_template, request, jsonify
from . import db as db_module
from flask_restful import Resource, Api, reqparse
from app.models import db, Lecturer, Tag, ContactInfo


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../instance/tourdeflask.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

db_module.init_app(app)

class LecturerListAPI(Resource):
    def get(self):
        #GET /lecturers
        lecturers = Lecturer.query.all()
        return [lecturer.to_dict() for lecturer in lecturers]

    def post(self):
        # POST /lecturers
        parser = reqparse.RequestParser()
        parser.add_argument('first_name', required=True, help="First name cannot be blank")
        parser.add_argument('last_name', required=True, help="Last name cannot be blank")
        parser.add_argument('contact', type=dict, location='json')  # Expecting a dictionary for contact
        parser.add_argument('title_before', store_missing=False, default='')
        parser.add_argument('middle_name', store_missing=False, default='')
        parser.add_argument('title_after', store_missing=False, default='')
        parser.add_argument('picture_url', store_missing=False, default='')
        parser.add_argument('location', store_missing=False, default='')
        parser.add_argument('claim', store_missing=False, default='')
        parser.add_argument('bio', store_missing=False, default='')
        parser.add_argument('price_per_hour', type=int, store_missing=False, default=0)
        data = parser.parse_args()

        contact_data = data.get('contact') or {}
        contact_info = ContactInfo(telephone_numbers=contact_data.get("telephone_numbers", []), emails=contact_data.get('emails', []))

        json_data = request.get_json()
        tag_data = json_data.get('tags', [])  # Defaults to an empty list if tags are not provided


        # Lecturer without tags
        lecturer_data = {key: data.get(key, '') for key in ['first_name', 'last_name', 'title_before', 'middle_name', 'title_after', 'picture_url', 'location', 'claim', 'bio', 'price_per_hour']}
        lecturer = Lecturer(**lecturer_data)
        lecturer.contact = contact_info

        db.session.add(contact_info)
        db.session.add(lecturer)

        # Handle tags
        for tag_item in tag_data:
            tag_name = tag_item.get('name')
            if tag_name:  # Check if 'name' key exists and is not empty
                existing_tag = Tag.query.filter_by(name=tag_name).first()
                if existing_tag:
                    lecturer.tags.append(existing_tag)
                else:
                    new_tag = Tag(name=tag_name)
                    db.session.add(new_tag)
                    lecturer.tags.append(new_tag)

        print(lecturer.tags)   
        db.session.commit()
        
        return lecturer.to_dict(), 200

class LecturerAPI(Resource):
    def get(self, uuid):
        # GET /lecturer/{uuid}
        lecturer = Lecturer.query.get_or_404(uuid)
        return lecturer.to_dict()

    def put(self, uuid):
        # PUT /lecturers/{uuid}
        lecturer = Lecturer.query.get_or_404(uuid)
        data = request.json

        # exclude tags from the data
        update_data = {key: value for key, value in data.items() if key not in ['tags', 'contact']}

        for key, value in update_data.items():
            setattr(lecturer, key, value)

        if 'contact' in data:
            contact_data = data['contact']
            if lecturer.contact:
                lecturer.contact.telephone_numbers = contact_data.get('telephone_numbers', [])
                lecturer.contact.emails = contact_data.get('emails', [])
            else:
                new_contact = ContactInfo(telephone_numbers=contact_data.get('telephone_numbers', []), emails=contact_data.get('emails', []))
                db.session.add(new_contact)
                lecturer.contact = new_contact

        # Handling tags
        if 'tags' in data:
            lecturer.tags.clear()
            for tag_name in data['tags']:
                tag = Tag.query.filter_by(name=tag_name).first() #search if tag with the name already exists
                if not tag:
                    # Create new tag if it does not exist
                    tag = Tag(name=tag_name)
                    db.session.add(tag)
                lecturer.tags.append(tag)

        db.session.commit()
        return lecturer.to_dict(), 200

    def delete(self, uuid):
        # DELETE /lecturer/{uuid}
        lecturer = Lecturer.query.get_or_404(uuid)
        db.session.delete(lecturer)
        db.session.commit()
        return '', 204

api.add_resource(LecturerListAPI, '/api/lecturers')
api.add_resource(LecturerAPI, '/api/lecturers/<uuid>')



app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)


try:
    os.makedirs(app.instance_path)
except OSError:
    pass
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    #return "Hello TdA :) "
    return render_template("index.html")
@app.route('/api')
def api():
    return { "secret":"The cake is a lie" }
@app.route('/lecturer')
def show_lecturer():
    return render_template("lecturer.html")


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    app.run()
