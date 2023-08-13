### AirBnB Clone Project - Command Interpreter README

## Description of the Project
Welcome to the AirBnB Clone Project! This project is the first step towards building a full web application that emulates the functionalities of Airbnb. The main objective of this phase is to develop a command interpreter that allows you to manage AirBnB objects efficiently. By completing this step, you'll set the foundation for the subsequent phases, which involve HTML/CSS templating, database storage, API integration, and front-end development.

## The key goals of this project are as follows:

Implement a parent class named BaseModel responsible for initializing, serializing, and deserializing instances of AirBnB objects.
Establish a straightforward serialization/deserialization process: Instance <-> Dictionary <-> JSON string <-> File.
Create specific classes for essential AirBnB objects (e.g., User, State, City, Place) that inherit from BaseModel.
Develop the initial storage engine, focusing on file storage.
Construct unit tests to validate all classes and the storage engine.
Description of the Command Interpreter
The command interpreter is an essential component of the AirBnB Clone Project. Similar to a shell, it allows you to manage AirBnB objects using a set of commands. These commands enable you to create, retrieve, update, and delete objects with ease.

## How to Start the Command Interpreter
To start the command interpreter, follow these steps:

Open your terminal or command prompt.
Navigate to the project directory containing the command interpreter files.
Run the command: ./console.py

## How to Use the Command Interpreter
Once you've launched the command interpreter, you can interact with it using a set of predefined commands. Here are some of the available commands and their usage:

create <class_name>: Creates a new instance of the specified class (e.g., User, State, City).
show <class_name> <object_id>: Displays information about the specified object.
all <class_name>: Lists all instances of the specified class or all classes if no argument is provided.
update <class_name> <object_id> <attribute_name> "<attribute_value>": Updates the specified attribute of the given object.
destroy <class_name> <object_id>: Deletes the specified object.

Examples


Creating a new User:
(hbnb) create User

Displaying information about a specific object:
(hbnb) show User 12345

Listing all instances of a class:
(hbnb) all State

Updating an attribute of an object:
(hbnb) update City 54321 name "New City Name"

Deleting an object:
(hbnb) destroy Place 98765