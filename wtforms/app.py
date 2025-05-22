from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, BooleanField, SelectField, RadioField, DateField, IntegerField, FloatField, DecimalField, DateTimeField, EmailField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, Length, Email
from secret_manager import Secret_Manager

secret_manager = Secret_Manager()
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_manager.get_secret_key()
class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=60)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    bio = TextAreaField('Bio', widget=TextArea(), validators=[DataRequired()])
    agree = BooleanField('I agree to the terms')
    role = SelectField('Role', choices= [('admin', 'Admin'), ('user','User')], default='user')
    gender = RadioField('Gender', choices = [('male','Male'), ('female', 'Female'), ('other','Other')])
    birth_date = DateField('Birth Date', format="%Y-%m-%d")
    event_datetime = DateTimeField('Event Date & Time', format="%Y-%m-%d %H:%M:%S")
    price = DecimalField('Price', places=2, rounding=None)
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    weight = FloatField('Weight')

@app.route('/', methods=['GET','POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('success'))
    return render_template('form.html',form=form)

@app.route('/success', methods=['GET','POST'])
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)