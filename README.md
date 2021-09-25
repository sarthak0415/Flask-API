# Flask API

This is a Flask API that I will keep improving with new features and functionalities.
This boilerplate can be used as a template for bigger projects.


### Getting started tutorial 
https://www.youtube.com/watch?v=s_ht4AKnWZg

### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [Flask](https://flask.palletsprojects.com/) - The framework used
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/) - REST docs

### Virtual environments

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
```

Install all project dependencies using:

```
$ pip install -r requirements.txt
```

### Running using Manager

This app can be started using Flask Manager. It provides some useful commands and configurations, also, it can be customized with more functionalities.

```
python manage.py runserver
```

Url generated - 
```
http://127.0.0.1:5000/api/
```

-------------

### Running
 
```
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ python -m flask run
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production.

If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

```
flask run --host=0.0.0.0
```