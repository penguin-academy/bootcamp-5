from operator import ne
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'thisisasecretkey'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_name = User.query.filter_by(
            username=username.data).first()

        if existing_user_name:
            raise ValidationError(
                "El nombre de usuario ya existe. Escoja otro.")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")


def guardar_usuario(un_usuario, un_password):
    import json
    with open("lista_user.txt","r") as archivo:
        contenido = archivo.readlines()
        print("conte:   ", contenido)
        users = json.loads(contenido[0])
        print("user_dict:", users)

    with open("lista_user.txt","w") as archivo:
        users[un_usuario]=un_password
        archivo.write(json.dumps(users))

    print("guardado")   

def chequear_password(un_usuario, un_password):
    import json
    with open("lista_user.txt","r") as archivo:
        contenido = archivo.readlines()
        print("conte:   ", contenido)
        users = json.loads(contenido[0])
        if users.get(un_usuario)==un_password:
            print("EXITO!")
            # Apagar amarillo
            # Prender verde
        else:
            print("password equivocado")
            # Apagar amarillo
            # Prnder rojo



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()


    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']

        chequear_password(username, password)

    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        guardar_usuario(username, password)
        #if form.validate_on_submit():
        # hashed_password = bcrypt.generate_password_hash(form.password.data)
        # new_user = User(username=form.username.data, password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()
        #return render_template('register.html', form=form)
    
    username=request.form.get('username')
    print("user: ", username, form.username, form)
    print("get param", request.args, request.args.get('username'))
    print("post param", request.form)

    return render_template('register.html', form=form)





"""
def lights_validation(state):
    '''
    Logic for turning lights depending on user's credentials validation 
    '''

    return None
"""

if __name__ == "__main__":

    #state = input("Ingrese estado")

    #lights_validation(state)
    app.run(debug=True)