# MongoDB CURD - Python FlaskApp

This is a simple example of Python Flask App for managing "Employee system details". The Database Management System is MongoDB. The python-MongoDB connector is PyMongo.

## Files included
- Read, Write, Update, delete mongodb document.
- Backup mongodb data into json file.
- Individual test input file for each CURD functions.

## Installation

First, you should install [MongoDB](https://docs.mongodb.com/manual/installation/)

then install all dependencies by running the following command:

```bash
 sudo pip install -r requirements.txt
```
It will install Flask and PyMongo.
## Usage
To run the program, first you should make sure MongoDB is running, start it using:
```cmd
$ sudo service mongod start

```
then, run the program:
```cmd
$ python main.py

```
Open your browser and go to localhost:5000 to see the running program.


