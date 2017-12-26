# db_create.py

from main import db
from models import Messages
from datetime import date


db.create_all()
db.session.commit()
