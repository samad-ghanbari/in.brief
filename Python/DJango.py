++++++++++++++++++++++++++++++++++ REQUIREMENTS

1-install python 3

2-install pip3   [pip=> python2   pip3=>python3]
    apt-get install python3-pip  (it is python package installer)
    
3- pip install virtualenv   (virtualenv is a tool to create an isolated Python environments)
4- virtualenv -p python3 DjangoEnv  (on the current directory create a virtual env with python 3 [with no parameter -p python3 it will uses default python])
5- cd ./DjangoEnv/bin
6- source activate  (we are on the virtual envirenment)
    [anything installed inside virtual env will located inside this folder not in the main system]



7- [inside virtual env] pip3 install -U django   (-U with all dependencies)
8- check django
    python3
        import django
        django.get_version()

9- install atom
10- goto edit > prefrences and add below packages:
        autocomplete-python  >> setting in extra path add : /home/samad/DjangoEnv/lib/python3.6;
        atom-python-virtualenv
        script (run codes)
        
11-virtualenv must be created in home directory in order to Atom recognise.

++++++++++++++++++++++++++++++++++ CREATE PROJECT WITH DJANGO

1- inside virtual env, brows to your favorite directory and run the below command:
        django-admin startproject PROJECT_NAME
                like : django-admin startproject testSite
                
2- inside folder :
        -manage.py (to create apps and ...)
        -a folder with the same name of project. files inside it are setting of all project
        - in case of app created its folder is here.
        
3- each app has a folder that contains all related files.

4- to create an app:
        python3 manage.py startapp app1

5- light python server for test (it is not powerfull server)
        python manage.py runserver

++++++++++++++++++++++++++++++++++    MODELS

Each model is a Python class that subclasses django.db.models.Model.
if class has no primary key django automatically create id field and set it as primary.
fields:
        AutoField
        BooleanField
        CharField
        IntegerField
        DateField

Field options:
         max_length  >> size of the VARCHAR
         null
         blank
         choices
         default
         help_text
         primary_key
         unique

relations:
        ForeignKey
        ManyToManyField
        OneToOneField 

for ordering we use class Meta
	class Meta
		ordering = ["field1"]

EXAMPLE:
        
        from django.db import models

        class myModel(models.Model):
            first_name = models.CharField("person's first name", max_length=30, primary_key=True) >> first parameter is verbose name
            id = models.AutoField(primary_key=True)  >> auto increment field
            last_name = models.CharField(max_length=30)
            serves_pizza = models.BooleanField(default=False)
            release_date = models.DateField()
            num_stars = models.IntegerField()

            SHIRT_SIZES = (
                        ('S', 'Small'),
                        ('M', 'Medium'),
                        ('L', 'Large'),
                              )
            shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)    >> automatically create select in html page

            MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
            medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)

            manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
            toppings = models.ManyToManyField(Topping)
            place_ptr = models.OneToOneField(Place, on_delete=models.CASCADE,  parent_link=True,  primary_key=True)
            
Using models (add app)
        once you have created your app, you should define it to the project: in project main setting folder edit settings.py
                INSTALLED_APPS = [
                                    #...
                                    'app1.apps.App1Config',
                                    #...
                                ]

Save Models on database
        python manage.py makemigrate appname   >> what will commit
        python manage.py migrate               >> commit


The manage.py startapp command creates an application structure that includes a models.py file.
If you have many models, organizing them in separate files may be useful.
To do so, create a models package. Remove models.py and create a myapp/models/ directory with an __init__.py file and the files to store your models.
You must import the models in the __init__.py file.
For example, if you had organic.py and synthetic.py in the models directory:

   myapp/models/__init__.py
        from .organic import Person
        from .synthetic import Robot

++++++++++++++++++++++++++++++++++ AUTO GENERATE MODELS

python manage.py inspectdb

python manage.py inspectdb > models.py

python manage.py inspectdb table1 > models.py

++++++++++++++++++++++++++++++++++ MODELS OBJECT

Assume than models are in a file mysite/blog/models.py

-create
        from blog.models import Blog
        b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
        b.save()
+++++++++++++++++++++++++++++++++++ MYSQL
pip install mysqlclient

# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}


# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8




---- or 


DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'danet',
            'USER': 'danet',
            'PASSWORD': '....',
            'HOST': 'localhost',
            'PORT': '3306',
    }
}

+++++++++++++++++++++++++++++++++++  QUERY

        python manage.py shell
-READ
[1]: from app1.models import model1, model2
[2]: q = model1.objects.all()  //  q = model1.objects.order_by('-field1')  >> -field1 , field1  ASC or DESC // q = model1.objects.all().count()  
[3]: q[0].id
[4]: q[0].fieldOfRecord

-INSERT
[1]: from app1.models import model1
[2]: from django.utils import timezone
[3]: q = model1(field1="..", field2=timezone.now() )
[4]: q.save()

-DELETE
[1]: from app1.models import model1
[3]: q = model1.objects.all()[0]
[4]: q.delete()

-----------------------
Model1 has a one to many relations with Model2
Model1-> primaryKey
Model2->foreignKey

m1 = Model1.Model2_set.create(Field1="...", Field2="..."); #create records by useing its parent
m2 = Model1.Model2_set.all(); # call all of its childern

----------------------
FILTER
Model1.objects.filter(field1="...")
or
Model1.objects.all().filter(field1="...")
or
Model1.objects.filter(field1="...").exclude(field2__gte=X).filter(...) # _gte  greater and equal than ..

Model.objects.get(pk=100)   record with primary key

-----------------------

FIELD LOOKUP
        __X

__lte    <=

__gte    >=

__exact   =

__iexact  like '%X%'

__contains  like

__pk__gt   >

----------------------
RAW Query

Model1.objects.raw("SELECT ....")

++++++++++++++++++++++++++++++++++  URL

in main settins > url.py
 >> patterns to views
 better to create  urls.py inside each app to be orgonised.
 use include to link urls
 
 insert
         app_name="app1"   > tell urls to be searched in which app
 
        urlpatterns = [
            path('admin/', admin.site.urls),
            path(r'^report/(?p<param1>[0-9])', views.report),   >>> view > report(param1)
            path(r'^install/', include('app1/urls')
        ]

-to use include we should use its library:  from django.conf.urls import include.
-to each path we can assign a name to use call it for convenience.
            
REGEX
 r'^admin/'

++++++++++++++++++++++++++++++++++ ADMIN

we just introduce models to admin (infact regiser models)
everything django handles.

each app contains a file named admin.py >> file to register models to manage database directly for that models.

# creating super user to login as admin
	python manage.py createsuperuser

#register models to admin.py

	in your app admin.py
		from . import models >> . is current directory

		admin.site.register(models.MODEL1)
		admin.site.register(models.MODEL2)

localhost:8888/admin
	login 
	>> can manage models

#Each record of a model(table) is an object of that model
	to clarify each record we could use a function to return distiguisher name for each record.
	it is done by useing function __str__() inside models

	def __str__(self)
		return self.name + " " + self.lastname  >>> each record representative instead of <object MODEL1>

# in model by using get_absolute_url(self) a button will appear in admin page which shows item on the site


####  Customising admin page by using predefined methods

1- ModelAdmin class 
	class has a suffix Admin and inherit of ModelAdmin

	in your app and admin.py we create a class for each model like below and then link register to that class
-method 1:
		class MODEL1Admin(admin.ModelAdmin)
			pass
		admin.site.register(models.MODEL1, MODEL1Admin)
		
		class AuthorAdmin(admin.ModelAdmin)
			pass

		admin.site.register(models.Author, AuthorAdmin)

-method 2 by decorators
		@admin.register(models.MODEL1)
		class MODEL1Admin(admin.ModelAdmin)
			pass

--- Customise parameters:
+list_display   >> which field to show on panel table
		@admin.register(models.MODEL1)
		class MODEL1Admin(admin.ModelAdmin)
			list_display=('field1','field2','field3')  >>>> here we can use model method that returns string

+list_filter  >> search panel
		@admin.register(models.MODEL1)
		class MODEL1Admin(admin.ModelAdmin)
			list_display=('field1','field2','field3')
			list_filter=('field2', 'field3')

+fields   >> categorize fields
		@admin.register(models.MODEL1)
		class MODEL1Admin(admin.ModelAdmin)
			list_display=('field1','field2','field3')
			list_filter=('field2', 'field3')
			fields = ['field1',('field2','field3'),('field4','field5')]

		here field1 in one group
		     field2 and field3 in one group
		     field4 and field5 in one group

+fieldsets   >> like fields but in better way. they are grouped in div with header

		@admin.register(models.MODEL1)
		class MODEL1Admin(admin.ModelAdmin)
			list_display=('field1','field2','field3')
			list_filter=('field2', 'field3')
			fieldsets = (	("Titl1", {fields:('field1')}), 
					(None, {fields:('field2', 'field3')}),
					("Titl2", {fields:('field4', 'field5')})
				     )


+inline Edit  >> ability to modify two table with relation in one page

in admin.py we create a class which inherit of admin.TabularInline or StackInline ...

	class ModelxInline(admin.TabularInline)
		model = models.MODEL2
		extra=1  >> default intance number


	@admin.register(models.MODEL1)
	class MODEL1Admin(admin.ModelAdmin)
		list_display=('field1','field2','field3')
		list_filter=('field2', 'field3')
		inlines=[ModelxInline]

++++++++++++++++++++++++++++++++++   TEMPLATES

template is similar to VIEW and  base template is Layout
each app must have its own template so we need to create a folder named templates and put index.html inside it

to prevent template confliction it is better to put our app template inside a folder of app name so like :  app_name/templates/app_name/index.html

there are two functions to load template
	1-	get_template(TEMPLATE_NAME, using=None)
	2-	select_template(TEMPLATE_NAME_LIST, using=None)   >>> it gets a list of template and select the first one that exists

### VARIABLES
variables are surrounded by {{}}  example : {{ VARIABLE }}
In html page:

	Je suis {{ My_Name }}. J`habite a {{ City }}.
	{'My_Name': "Samad", "City":"Teheran"}   >> context is a dictionary

		>>> Je suis Samad. j`habite a teheran.

### TAGS
it provides arbitrary logics in the rendering process. its usage are for : if for while ...
{% %}....{% %}

	{% for x in list%}......{% endfor %}


### FILTERS
they transform the value
{{ my_date | date:Y-m-d}}
...


### Template render Context

from django.template import loader, Context

template = loader.get_template("template.html")

Context = Context(
		  {
			'param1': "Value1",
			'param2': "Value2"
		  }
		 )

template.render(Context)

### SHORTCUT

from django.shorcuts import render

render(request, 'Template.html', {'param1': "value1"})

### Generic Template
all templates inherit from the base template.

-base template:
  base.html

	<!DOCTYPE html>
	<html lang='eng'>
			....
		<head>
			{% block title %}
				...
			{% endblock %}
		</head>

		<body>
			{% block sidbar %}
			{% endblock %}

			{% block content %}
			{% endblock %}
		</body>

	</html>


- other templates:
	{% extends 'base.html' %}

	{% block sidbar %}...... {% endblock%}

	{% block content %} ... {% endblock %}


++++++++++++++++++++++++++++++++    VIEW
Views in fact are our controllers
	ROUTES <==> CONTROLLERS

- create a url for our own app. include it in main project urls.
- in app urls:

        from . import views
        app_name="app1" 
        urlpatterns = [
            path(r'^$/', views.index, name="index"), >> it will open view and run index method
            path(r'^(?p<id>[0-9]+)/)$', views.detail, name='detail') >> capture id and pass it to detail method
        ] 


view.py
            from django.shortcuts import render          >>>>> render automatically goes into templates folder
            from django.http import HttpResponse, HttpResponseRedirect
            
            def index(request)  >> all methods inside view must have parameter request in first
                    return HttpResponse("my index html")


            def detail(request, id)
                    return HttpResponse("my detail html with id "+id)

            
           def detail(request, id)
                    val1 = request.POST['form_field']
                    model = models.MODEL1.objects.all()
                    context={'model': model}
                    return render(request, 'detail', context)

          def detail(request, id)
                    record = get_object_or_404(MODEL1, pk=id) >>> get one record of model or return 404 not found  >>> in library shortcuts
                    return render(request, 'detail', {'record' : record})
-to redirect
          def detail(request, id)
                    return HttpResponseRedirect(reverse('app_name:XXX', args=(id))



---- class-based view
- instead of using methods in view we use a class
                                                
from django.views import generic
class indexView(generic.ListView)
        template_name = "app_name/index.html"
        context_object_name = 'my_context'  >> name that template uses

        def get_gueryset(self)
                return Model.objects.order_by('-field1')[:10]

also in urls
       path(r'^$/', views.indexView_as_view(), name="index") // a method that converts class to view

++++++++++++++++++++++++++ CSRF
            when using form with method post

            <form action="{% url app_name::detail id %}" method='post'>   // send id too
            {% csrf_token %}

+++++++++++++++++++++++++++++++++++++++++++ REMOVE DEFAULT APPS

-from setting.py of project remove INSTALLED_APP, middlewares, templates
-from urls.py remove import admin

+++++++++++++++++++++++++++++++++++++++++++

