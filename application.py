from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField,TextAreaField
from wtforms.fields import DateField, EmailField, TelField
from wtforms.validators import InputRequired

application = app = Flask(__name__,template_folder='template')
app.config['SECRET_KEY']='some_random_secret'

class SignUpForm(FlaskForm):
    name=StringField('Enter your Name',validators=[InputRequired()])
    email=EmailField('Enter your email',validators=[InputRequired()])
    publicity=RadioField('How did you hear about us ?',choices=[('social','Social Media'),('poster','Posters and flyers')])
    feedback=TextAreaField('Anything else you want to tell us ?')
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def hello_world():

    form = SignUpForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['publicity'] = form.publicity.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("thankyou"))
    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
 
    return render_template('thankyou.html')

if __name__ == '__main__':
    application.run('localhost',8080,debug=True)
