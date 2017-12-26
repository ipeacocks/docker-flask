from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

import datetime

from forms import MessageForm

################ 
#### config #### 
################

app = Flask(__name__)
app.config.from_pyfile('_config.py')
db = SQLAlchemy(app)

from models import Messages

################ 
#### routes #### 
################

def list_messages():
    return db.session.query(Messages).order_by(Messages.message_date.desc())


@app.route("/", methods=['GET','POST'])
def main():
    error = None
    form = MessageForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_message = Messages(
                datetime.datetime.utcnow(),
                form.message.data
            )
            db.session.add(new_message)
            db.session.commit()
            return redirect(url_for('main'))
    return render_template(
        'main.html',
        messages=list_messages(),
        form=form,
        error=error
    )
