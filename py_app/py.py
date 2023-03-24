from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # check if the email and password are correct
        if form.email.data == 'email@example.com' and form.password.data == 'password':
            return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/home')
def home():
    return '<h1>You are now logged in!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
