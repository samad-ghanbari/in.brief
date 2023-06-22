++++++++++++++++++++++++++++++++++++++++ requirements
1-install python 3

2-install pip3   [pip=> python2   pip3=>python3]
    apt-get install python3-pip  (it is python package installer)
    
3- pip install virtualenv   (virtualenv is a tool to create an isolated Python environments)
4- virtualenv -p python3 flaskEnv  (on the current directory create a virtual env with python 3 [with no parameter -p python3 it will uses default python])
5- cd ./flaskEnv/bin
6- source activate  (we are on the virtual envirenment)
    [anything installed inside virtual env will located inside this folder not in the main system]



7- [inside virtual env] pip3 install -U flask   (-U with all dependencies)
8- check flask
    python3
        import flask
        flask.__version__

9- install atom
10- goto edit > prefrences and add below packages:
        autocomplete-python  >> setting in extra path add : /home/samad/flaskEnv/lib/python3.6/site-packages;
        atom-python-virtualenv
        script (run codes)
	tool-bar
	too-bar-atom
        
11-virtualenv must be created in home directory in order to Atom recognise.

MVC:
        Models      >> for database >> lib: sqlalchemy
        Controllers >> Routes
        Views       >> Templates   >> engin : Jinja2
++++++++++++++++++++++++++++++++++++++++ crate Project with flask
create a file for example index.py

        from flask import Flask    >> load flask
        app = Flask(__name__)      >> create an instance of flask
         
        @app.route('/')            >> create a route  
        def hello_world():         >> controller to url http://siteAddress/
            return 'Hello World!'
         
        if __name__ == '__main__': >> in case file execute itself run the app. if it is a module of another app it will not run.
            app.run()

- now on terminal:  python3 index.py

- we give parameters for run method:
        app.run(host='0.0.0.0', port=8080, debug=True)
        
++++++++++++++++++++++++++++++++ APP SECRET KEY

app.config['SECRET_KEY']="kjhkjhkj"

>> import os
   os.urandom(24)
++++++++++++++++++++++++++++++++ ROUTE
urls are recognised by their method names.
-using decorator
        @app.route('/')  >> decorator   >> this url name is home   so its link :   {{ url_for('home') }}
        def home(): 
            return ('home page')

        @app.route('/report')
        def report():
            return redirect( url_for('home') )
        
        
-add url rule
        def home(): 
            return ('home page')
        app.add_url_rule('/', view_func=home) >> just method name

+++++++++++++++++++++++++++++++++++++++++  VARIABLES IN ADDRESS
-variables can be introduced by <var1>
-convertion can be done by:  <int:var1>   it means read var1 and convert it to int

        from flask import Flask
        app = Flask(__name__)
         
        @app.route('/user/<username>')
        def show_user_profile(username): 
            # show the user profile for that user
            return (f'User {username}')
            
        @app.route('/post/<int:post_id>')
        def show_post(post_id):
            # show the post with the given id, the id is an integer
            return (f'Post {post_id}')
            
        @app.route('/path/<path:subpath>')
        def show_subpath(subpath):
            # show the subpath after /path/
            return (f'Subpath {subpath}')
                
        app.run()


+++++++++++++++++++++++++++++++++++++++++ GET & POST
        from flask import request // url_for, redirect, render_template, flash
         
        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if request.method == 'POST':
                name = request.form.get("name", "")
                name = request.form["name"]
                age = request.form.get("age", "")
                response = "Hey there {}! You said you are {} years old.".format(name, age)
                return response
            else:
                return show_the_login_form()

++++++++++++++++++++++++++++++++++++++++ TEMPLATES JINJA2
in the main route of project we should create two folder
        -templates   >> put html files
        -static      >> put css & js  >> in addressing : {{ url_for('static', filename='style.css') }}

to render template we use a method
        render_template("a.html")
--------------
JinJa:
#1       {% %}       statements  >> default
#2       {{ var1 }}  print values
#3       {# #}       comments
#4       arbitrary     line statement

to enable line statement

        app.jinja_env.line_statement_prefix="#"
        
no we can use:
        # for i in list
                {{ i }}
        # endfor
---------------
jinja filters
 {{ var1 | e }}       >>> escape 
 {{ var2 | d(123) }}  >>> set default value
 ...
 
--------------
example:
        temp/temp.py

        from flask import Flask, render_template
 
        app = Flask(__name__)
         
        @app.route("/")
        @app.route("/home")
        @app.route("/index")
        def index():
            return render_template('home/home.html', var1='samad', var2=123)
            
        @app.route("/user")
        def welcome():
            return render_template('user/user.html')

        if __name__ == '__main__':
            app.run()


temp/templates
        -base.html
        -user/user.html
        -home/home.html

-base.html
        <!DOCTYPE html>
        <html>
                <head>
                <title>{% block title %}{% endblock %}</title>   >>> jinja 
                </head>

                <body>
                <h1> MY TEMPLATE</h1>
                {% block body %}{% endblock %}
                </body>
        </html>

-user.html
        {% extends 'base.html' %}

        {% block title %}

        USER -TITLE

        {% endblock %}


        {% block body %}
        <h2> USER BODY </h2>
        {% endblock %}

-home.html
        {% extends 'base.html' %}

        {% block title %}
         HOME -TITLE
        {% endblock %}


        {% block body %}
        <h2> HOME BODY </h2>
        <h3>{{ var1 }}</h3>
        <h3>{{ var2 }}</h3>
        {% endblock %}


++++++++++++++++++++++++++++++++ DEBUG
to view error in web browser we should run app while debugger enabled.

        app.run(debug=True)
        
+++++++++++++++++++++++++++++++++ ERROR HANDLER

in case of error 404 this page will displayed

@app.errorhandler(404)
def error404(error)
        return render_template('errors/e404.html')

+++++++++++++++++++++++++++++++++ FLASH

from flask import flash

...
flash("flash message on refresh it will disappear")


in html file:

        {% with message = get_flashed_messages() %}
                {% if message %}
                        {% for msg in message %}
                                {{ msg }}
                        {% endfor %}
                {% endif %}

        {% endwith%}


++++++++++++++++++++++++++++++++ DATABASE
ORM for flask is SQLAlchemy
pip install flask_sqlalchemy
%%%%%%%%%%%%%%%%%%%%%  SQLITE

pro1.py
        from flask_sqlalchemy import SQLAlchemy
        import os
        from sqlachemy import desc

        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, 'DB.db')
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db = SQLAlchemy(app)

        from models import tbl1

--new record:
        rec = tbl1(field1=1, field2="..", field3="...")

        db.session.add(rec)
        db.session.commit()

-- read table:
        objs = tbl1.query.all()
        objs = tbl1.query.order_by(desc('field2')).all()
        obj = tbl1.query.filter_by(field1="...").first()  >>> get one record


??? flask-script

-create a file named models.py in the root of project.

        from pro1 import db

        class tbl1(db.Model):
                field1 = db.Column(db.Integer, primary_key=True)
                field2 = db.Column(db.Text)
                field3 = db.Column(db.String(50), unique = True)
                
        def __repr__(self) :       >> similar __str__ in django representative of object
                return self.field2


%%%%%%%%%%%%%%%%%%%%%%%% MYSQL
pip install flask-mysql

        from flask_mysqldb import MySQL
        app.config['MYSQL_HOST'] = 'localhost'
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'root'
        app.config['MYSQL_DB'] = 'MyDB'
	app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

        mysql = MySQL(app)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()

%%%%%%%%%%%%%%%%%%%%%%% MODEL
	from flask import Flask, render_template
	from flask_sqlalchemy import SQLAlchemy
	from models import User;


	app = Flask(__name__)

	app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://danet:pass....@localhost/danet"
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   >> it makes some overhead

	db = SQLAlchemy(app)

	@app.route('/')
	def index():
	    objs = User.query.all()
	    return render_template('users.html', cursor=objs);


	if __name__ == '__main__' :
	    app.run(debug=True)#debug=True

++++++++++++++++++++++++++++++++++  CREATE MODEL FROM DATABASE

-install library:
        pip install flask-sqlacodegen

        flask-sqlacodegen --flask --outfile models.py mysql+pymysql://user-name:password@host:port/db-schema

        flask-sqlacodegen --flask --outfile models.py --tables "Schedule,ScheduleType" mysql+pymysql://user-name:password@host:port/db-schema

example:
	flask-sqlacodegen --flask --outfile user_model.py --table "users" mysql://danet:Danet@Samad.2514@localhost:3306/danet


++++++++++++++++++++++++++++++++++++++++++++FORM VALIDATION
it is done by extension WTFORM

install:
        pip3 install Flask-WTF

myforms.py:
                from flask_wtf import Form
                from wtforms.fields import StringField, PasswordField, TextAreaField, IntegerField, SelectField
                from wtforms.validators import DataRequired, Email, IPAddress, regexp ...

                class myform1(Form)
                        field1 = StringField("place holder text", validators=[DataRequired()])
                        field2 = TextAreaField("ph", validators=[DataRequired()])
			
			password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
		        confirm  = PasswordField('Repeat Password')
        

in app file:
        from myforms import myform1

        ..
        @app.route('/add')
        def add():
                form1 = myForm1()
                return render_template('form.html', form=form1)

form.html:
	{{ form.username(class="form-control", id="username") }} >>> <input ....>

        {{ form.field1(class="", id="")  }} >> this will create input field  // form.field1.errors

+++++++++++++++++++++++++++++++++++  AUTHENTICATION

-module:
        flask-login  :   pip install flask-login

-decorator:
        @login_required
        
--USAGE:
        from flask_login import LoginManager, login_required, login_user , logout_user, current_user 

        login_manager = LoginManager()
        login_manager.session_protection = "strong"
        login_manager.init_app(app)

        @app.route(/home)
        @login_required     >> user must logged-in  >> error 401: unahorized
        def home():
                ...

        @app.route(/logout)
        def logout():
                logout_user()  >> method destroy the session
        
---- UserMixin module
        from  flask_login import UserMixin
                 >> this module has some method about user like is_active is_anonimous ...

        current_user >> is an object of logged-in user
                f = current_user.field1

our user table inherit from UserMixin so in template we can user:
        if current_user.is_authenticated():
                ...
++++++++++++++++++++++++++++++++++++++ HASH
        from werkzeug.security import check_password_hash , generate_password_hash

        pass = generate_password_hash(pass)

        check_password_hash(self.pass, inp_pass)  >> returns true or false

        user = tbl1.query.filter_by(user="").first()
        if user is not None and user.check_password_hash(inp_pass):
                login_user(user)
                
+++++++++++++++++++++++++++++++++++++ RESTFUL
 return json

        from flask import jsonify
        return jsonify( [{json...}] )

+++++++++++++++++++++++++++++++++++++ BLUEPRINT
for big project we`d better to use blueprint.

- /main.py
	from flask import Flask
	from app1.app1 import app1

	app = Flask(__name__)
	app.debug = True

	app.register_blueprint(app1, url_prefix='/app1')

	@app.route('/')
	def home():
	    return 'App home'

	if __name__ == '__main__':
	    app.run()

- /app1/app1.py

	from flask import Blueprint
	app1 = Blueprint('app1', __name__) # can define templates folder and static folder
	def before_myblueprint():
		...
    		return redirect( url_for('home') )

	app1.before_request(before_myblueprint)
	

	@app1.route('/')
	def index():
	    return "blueprint page"



++++++++++++++++++++++++++++++++++++++++ AJAX
	from flask import Flask, render_template, jsonify, request


	app = Flask(__name__)

	@app.route('/')
	def index():
	    return render_template('temp.html');

	@app.route('/ajaxReq', methods=["POST"])
	def ajaxReq():
	    text =request.form['param'];
	    data={'text':text}
	    return jsonify(data)


	if __name__ == '__main__' :
	    app.run(debug=True)#debug=True


%%%%%%%%%%%%%%%%%%%

	<script>
	  function clicked()
	  {
	    $.ajax({
		url : "{{url_for('ajaxReq')}}" ,
		data: {"param": "Samad Ghanbari"},
		type: 'POST',
		success: function(data)
		{
		  document.getElementById("myTxt").innerText = data['text'];
		}
	    });
	  }
	</script>

++++++++++++++++++++++++++++++++++++++++++ 
