from app import app, db
from app.forms import UserForm
from app.models import User
import sqlalchemy as sa
from flask import render_template, request


@app.route('/', methods = ['GET', 'POST'])
@app.route('/index', methods = ['GET', 'POST'])
def index():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
            username = form.username.data
            password = form.password.data


            user = User(username = username, password = password)

            db.session.add(user)
            db.session.commit()
        

    return render_template('index.html', title='User Form', form=form)