from app import app, UserForm

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    form = UserForm()
    return render_template('index.html', title='User Form', form=form)