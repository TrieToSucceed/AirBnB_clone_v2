# HBNB

This is the console /command interpreter for the Holberton Airbnb clone project. The console can be used to store objects in and retrieve objects from a JSON file.

### Additional features include:
* implementation of MySQL database using SQLAlchemy
* contains scripts to deploy static html/css code to web server

### Supported classes:
* BaseModel
* User
* State
* City
* Amenity
* Place
* Review

### Commands:
* create - create an object
* show - show an object (based on id)
* destroy - destroy an object
* all - show all objects, of one type or all types
* quit/EOF - quit the console
* help - see descriptions of commands

To start, navigate to the project folder and enter `./console.py` in the shell.

#### Create
`create <class name>`
Ex:
`create BaseModel`

#### Show
`show <class name> <object id>`
Ex:
`show User my_id`

#### Destroy
`destroy <class name> <object id>`
Ex:
`destroy Place my_place_id`

#### All
`all` or `all <class name>`
Ex:
`all` or `all State`

#### Update
`update <class name> <object id> <key> <"value">`  
Ex:  
`update User my_user_id name "Jinji"`

#### Quit
`quit` or `EOF`

#### Help
`help` or `help <command>`
Ex:
`help` or `help quit`

Additionally, the console supports `<class name>.<command>(<parameters>)` syntax.
Ex:
`City.show(my_city_id)`

## Authors
[Jian Huang](http://github.com/trieToSucceed/) 
[Jinji Zhang](https://github.com/iamzinzi/)

## Originally Forked From
[Kevin Yook](https://github.com/yook00627)'s [AirBnB-clone-1](https://github.com/yook00627/AirBnB_clone) as part of Holberton School's AirBnB Clone Project

## Learning Objectives
* What is Unit testing and how to implement it in a large project
* What is *args and how to use it
* What is \**kwargs and how to use it
* How to handle named arguments in a function
* How to create a MySQL database
* How to create a MySQL user and grant it privileges
* What ORM means
* How to map a Python Class to a MySQL table
* How to handle 2 different storage engines with the same codebase
* How to use environment variables
