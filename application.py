from flask import Flask, url_for, render_template, request, Response, redirect, make_response
from flask_static_compress import FlaskStaticCompress
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os
import subprocess

class MyForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    bitmoji = StringField('bitmoji', validators=[DataRequired()])
    background = StringField('background', validators=[DataRequired()])

application = Flask(__name__, static_folder='static', template_folder='templates')

SECRET_KEY = os.urandom(32)
application.config['SECRET_KEY'] = SECRET_KEY


@application.route("/")

@application.route('/', methods=('GET', 'POST'))
def home():
    form = MyForm()
    if form.validate_on_submit():
        #gets data from form about username and colors
        bitmoji = form.bitmoji.data
        background = form.background.data
        username = form.username.data
        with open(os.devnull, 'wb') as devnull:
            subprocess.check_call(['python', 'getCode.py', username, bitmoji, background], stdout=devnull, stderr=subprocess.STDOUT)
        return redirect('')
    return render_template('index.html', form=form)
if __name__ == "__main__":
    application.run(debug=True)
