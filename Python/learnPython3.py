#print string

print("string is %s and the integer is %d and the float number is %f " %('hello', 23, 34.53));

print("string is {1:s} and the integer is {0:d} and the float number is {3:f} ".format(23,'hello', 23, 34.53));

print("string is {} and the integer is {} and the float number is {} ".format('hello', 23, 34.53));

str = "string is $%s and the integer is $%4d and the float number is $%5.2f " %('hello', 23, 34.53);
print(str)

print('''hello
my name is
samad''')

print("hello \t world")
print(r'hello \t world') # raw string 
print('Hello world'.replace('world', 'universe'))

print("-------------------------------------------------")
a = "24"
b = int(a)
print("{}".format(b))

a= 34.32
b = int(a);
print("{}".format(b))


a= "34.32"
b = float(a);
print("{}".format(b))

print("-------------------------------------------------LIST >>> bracets")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(a[0])
print(a[1])


b = a[0:3]
print(b)
b = a[1:3]
print(b)

b = a[2:9:2]
print(b)



b = a[:2]
print(b)


b = a[3:]
print(b)



a = []
print(a)
a.append(10)
a.append(20)
a.append(30)
a.append('samad')
print(a)
del a[1]
print(a)
print(a[-1]) # from the last, the first one
print(a[-2]) # from the last, the second one

print("-------------------------------------------------Tuples >> prantes")

a = ('jan', 'feb', 'march', 'apr', 'may') # it is fixed and cannot be changed
print(a)
#a.append('jun') NO APPEND
#a[1] = 'jjan'; NO ASSIGNEMENT
print(a[0])
print(a[-1])
print("-------------------------------------------------Dictionary")
a = {'samad': 1, 'ali': 2, 'mohamad':3, 'samad':4}
print(a)


a = dict(samad=1, ali=2)
print(a)

print(a['samad'])
print(a.get('samad'))


for x in a.values():
    print(x);

for x in a.keys():
    print(x);

for x,y in a.items():
    print(x,y)

del a['samad'];
print(a)

a['mohamad']=3
a['hasan']=4
print(a)

print("-------------------------------------------------Input")
a = input("Enter your name: ");
age = input("Enter your age: ");
print("Your Name is "+a+" and you are ",age," years old."); # both of these are possible


print("-------------------------------------------------if")
a = input("Enter your name : ");
if a == 'samad':
    print('Hello samad')
    print ('hello again')
else:
        print("goodby")

if a == 'samad':
    print('Hello samad')
    print ('hello again')
elif a == 'sa':
        print("goodby")
else:
    print("elif else")
        
print("-------------------------------------------------inline if")

a = 24 if a==24 else 26 
print(a) # 26


print(24 if 1==1 else 25)
print(24 if 1==2 else 25)

print("-------------------------------------------------for")
a = [1, 2, 3, 4, 5, 6]
for x in a:
    print(x)
    print(x*x)

for i in range(1, 10, 2):
    print(i)

print("-------------------------------------------------while")

a = 5
while a > 0:
    print(a)
    a = a -1

print("-------------------------------------------------try except")
a = 2
b = 0

try:
    a = a/b
except ValueError:
    print("value error")
except ZeroDivisionError:
  print("Zero Division")
except Exception as e:
    print(e)
print("-------------------------------------------------Function")
def checkit(number):
	for x in range(2,number):
		if (number % x) ==  0:
					return False;
	return True;

a= checkit(5)
if a :
	print("it is a prime  number.")
else:
	print("it is not a prime number.")
print("-------------------------------------------------import")
# module file:    prime.py
"""def checkit(number):
	for x in range(2,number):
		if (number % x) ==  0:
					return False;
	return True;

# main module 
 import prime
# use:
prime.checkit(5) ...

# if the prime.py is not in the same directory we need to add it to system path
# main module file   main.py
 import sys
 if 'PATH like /home/samad/pythonModule/' not in sys.path:
	sys.path.append('/home/samad/pythonModule/');
import prime"""
print("-------------------------------------------------files")

file = open('./learnPython3.py', 'r') # r:readonly w:writeonly a:append r+:read&write
#in w mode if file dose not exists it will create it
line1 = file.readline(); # file.read(10) >> 10 byte of files will read
line2 = file.readline();
line3 = file.read(20);
print(line1);
print(line2);
print(' ------- 20 byte of file')
print(line3);
file.close();

#
file = open('./learnPython3.py', 'r') # r:readonly w:writeonly a:append r+:read&write
for line in file:
	line = file.readline();
#	print(line);
file.close();
"""
#append
file = open('./file.txt', 'a') it opens file end moves to the end of file
file.write('.....')
file.close()

#  binary file mode:   rb  wb
IN = open('a.jpg', 'rb')
OUT = open('b.jpg', 'wb')
msg = IN.read(10)
while len(msg):
	OUT.write(msg)
	msg = IN.read(10)
IN.close();
OUT.close();
"""
print("-------------------------------------------------Database MYSQL")
#   apt-get install python3-mysql.connecotr   ---python-mysql.connecotr is for python2
# https://dev.mysql.com/downloads/windows/ >>> mysql connector  >> connector/python
import mysql.connector
db = mysql.connector.connect(user='USER', password='PASS', host='127.0.0.1', database='danet')
print(db)

Cursor = db.cursor()
Cursor.execute("SELECT * FROM `users` WHERE 1");
for x in Cursor:
  print(x)

#-----
print("_____________________")
#sql = "SELECT * FROM `users` WHERE name=%s"
#val = ("samad")
#Cursor.execute(sql, val)
sql = "SELECT * FROM `users` WHERE name='{}'".format('samad')
print(sql)
Cursor.execute(sql) # executemany(sql, val) >> val: array
res = Cursor.fetchall()
for row in res:
  print(row)

for row in res:
    print(row[0], " ", row[1] )

# if query changes dabase we need to write db.commite()  to make changes in database

db.close()


#######################################################
#		CLASS
class Person:
  def __init__(self, name, age):# built-in function
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 

# there is no private and protected variabled in python but by convention:
	variables start with _ >> protected
	variables start with __ >> private

so :
	self.__privateValue = "samad" 

#------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 
#---------------------------
#The self parameter is a reference to the class itself, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

#-------------------------

important packages:

- NumPy : 
    Advanced array operations (e.g. add, multiply, slice, reshape, index).
    Comprehensive mathematical functions.
    Random number generation.
    Linear algebra routines.
    Fourier transforms, etc.

- pandas
	
    Reading/writing data from/to CSV and Excel files and SQL databases.
    Reshaping and pivoting datasets.
    Slicing, indexing, and subsetting datasets.
    Aggregating and transforming data.
    Merging and joining datasets.

- Matplotlib
	Matplotlib is the most common data exploration and visualization library.
	You can use it to create basic graphs like line plots, histograms, scatter plots, bar charts, and pie charts. 
	You can also create animated and interactive visualizations with this library.
	Matplotlib is the foundation of every other visualization library.
	
- Seaborn
	Seaborn is a high-level interface for drawing attractive statistical graphics with
	just a few lines of code. Let's see it in action.
	
	
- Requests
	This library is designed to make HTTP requests with Python more responsive and user friendly.
	The intuitive JSON method offered by Requests helps you avoid manually adding query strings to URLs. 
	With Requests, you can:
    Customize, inspect, authorize, and configure HTTP requests.
    Add parameters, headers, and multi-part files.
    Decompress data automatically.
    Upload multiple files at the same time.

- urllib3
	urllib3 is another user-friendly HTTP client for Python

- NLTK
	Natural Language Toolkit (NLTK) is one of the leading Python platforms for processing language data.
	It is a set of language processing libraries and programs that provide a toolkit for:

    Classification.
    Tokenization.
    Stemming.
    Tagging.
    Parsing.
    Semantic reasoning.


- Pillow
	
    Open and save images of different file types (JPEG, PNG, GIF, PDF, etc.).
    Create thumbnails for images.
    Use a collection of image filters (e.g. SMOOTH, BLUR, SHARPEN).

- 


