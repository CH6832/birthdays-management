# Birthday Manager

## :newspaper: About the project

Birthday Manager is a simple web application built with Flask that allows users to add and manage birthday entries in a database. Users can add names along with their corresponding birth months and days, and view all stored entries.

### Content overview

    .
    ├── docs/ - documentation sources
    ├── instance/ - database
    ├── migrations/ - generated migrations scripts byFlask-Migrate. Files in there should be deleted when database has to be generated from scratch.
    ├── static/ - contains static files (css, js)
    ├── templates/ - contains html templates
    ├── tests/ - all kinds of test scripts
    ├── app.py - flask application and program entry
    ├── LICENSE - license file
    ├── README.md - project descriptions and instructions
    └── requirements.txt - project requirements

## :notebook: Features

* Add and delete new birthday entries.
* View all stored birthday entries.
* Simple and intuitive user interface.

## :runner: Getting started

### Prerequisites

0. Clone the repository:

```sh
git clone https://github.com/CH6832/birthdays-management.git
```

1. Extract the repository:

```sh
tar -xf birthdays-management.zip
```

2. Navigate into root directory:

```sh
cd birthdays-management
```

3. Install requirements:

```sh
pip3 install -r requirements.txt
```

### Run the application

0. Run script to see how it works:

```sh
python main.py "tests\\test_script.py"
```

### Run the application in a Docker container:

0. Build the docker image

```sh
docker build -t flask-app .
```

1. Run the docker container:

```sh
docker run -d -p 5000:5000 flask-app
```

2. FLask application is now running in a docker container reachable in your webbrowser:

```sh
http://localhost:5000
```

### Update the `instance\birthdays_db.db` file because of db model changes

0. Make changes to 'UserModel' class in `app.py`

1. Generate migration scripts in `migrations` folder:

```sh
flask db migrate -m "describe your changes"
```

2. Apply the migrations:

```sh
flask db upgrade
```

## :books: Resources used to create this project

* Python
  * [Python 3.12 documentation](https://docs.python.org/3/)
  * [Built-in Functions](https://docs.python.org/3/library/functions.html)
  * [Python Module Index](https://docs.python.org/3/py-modindex.html)
  * [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
  * [ast — Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)
  * [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)
  * [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)
* Markdwon
  * [Basic syntax](https://www.markdownguide.org/basic-syntax/)
  * [Complete list of github markdown emofis](https://dev.to/nikolab/complete-list-of-github-markdown-emoji-markup-5aia)
  * [Awesome template](http://github.com/Human-Activity-Recognition/blob/main/README.md)
  * [.gitignore file](https://git-scm.com/docs/gitignore)
* Editor
  * [Visual Studio Code](https://code.visualstudio.com/)

## :bookmark: License

This project is licensed under the terms of the [MIT License](LICENSE).
