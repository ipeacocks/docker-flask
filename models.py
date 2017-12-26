from main import db
import datetime


class Messages(db.Model):

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, primary_key=True)
    message_date = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    message_body = db.Column(db.String, nullable=False)

    def __init__(self, message_date, message_body):
        self.message_date = message_date
        self.message_body = message_body

    def __repr__(self):
        return '<message_id {0}>'.format(self.message_id)
