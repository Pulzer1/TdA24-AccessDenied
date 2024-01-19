from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()

class Tag(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {"uuid": self.uuid, "name": self.name}

class ContactInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    telephone_numbers = db.Column(db.PickleType)  # Storing as list
    emails = db.Column(db.PickleType)  # Storing as list

    def to_dict(self):
        return {
            "telephone_numbers": self.telephone_numbers,
            "emails": self.emails
        }

class Lecturer(db.Model):
    uuid = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    title_before = db.Column(db.String(80))
    first_name = db.Column(db.String(80), nullable=False)
    middle_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80), nullable=False)
    title_after = db.Column(db.String(80))
    picture_url = db.Column(db.String(255))
    location = db.Column(db.String(100))
    claim = db.Column(db.Text)
    bio = db.Column(db.Text)
    price_per_hour = db.Column(db.Integer)
    contact_id = db.Column(db.Integer, db.ForeignKey('contact_info.id'))
    contact = db.relationship('ContactInfo', backref='lecturers')
    tags = db.relationship('Tag', secondary='lecturer_tags', lazy='subquery',
                           backref=db.backref('lecturers', lazy=True))

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "title_before": self.title_before,
            "middle_name": self.middle_name,
            "title_after": self.title_after,
            "picture_url": self.picture_url,
            "location": self.location,
            "claim": self.claim,
            "bio": self.bio,
            "price_per_hour": self.price_per_hour,
            "contact": self.contact.to_dict(),
            "tags": [tag.to_dict() for tag in self.tags]
        } 

lecturer_tags = db.Table('lecturer_tags',
    db.Column('lecturer_uuid', db.String(36), db.ForeignKey('lecturer.uuid'), primary_key=True),
    db.Column('tag_uuid', db.String(36), db.ForeignKey('tag.uuid'), primary_key=True)
)