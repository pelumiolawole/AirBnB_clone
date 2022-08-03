# AirBnB_clone

 <iframe src="https://gifer.com/embed/94Vr" width=480 height=480.000 frameBorder="0" allowFullScreen></iframe><p><a href="https://gifer.com">via GIFER</a></p>

<h3 align="center">Airbnb Clone</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/pelumiolawole/AirBnB_clone/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/pelumiolawole/AirBnB_clone/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> ALX project
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

This is the first step towards building our first full web application: the AirBnB clone. This is a project that is built with the aim to learn and apply concepts of high level programming and software engineering in general. 

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Python3

### Installing

Clone this reposito

```
git clone git@github.com:pelumiolawole/AirBnB_clone.git
cd AirBnB_clone
./console.py
```

## 🔧 Running the tests <a name = "tests"></a>

This project uses the python unittest model for automated tests


#### Run all unit tests
`python3 -m unittest discover tests`

#### Run a test from a specific file
`python3 -m unittest tests/tespytestt_models/test_base_model.py`

## 🎈 Usage <a name="usage"></a>

You can run the schell (in an interactive or non-interactive mode) to manipulate your models.
You can start it from running the console.py file:

```
$ ./console.py
```

The following commands are supported:

### create: 
  Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. 
  Ex: 
  ```
  $ create BaseModel
  ```

### show: 
  Prints the string representation of an instance based on the class name and id. 
  Ex: 
  ```
  $ show BaseModel 1234-1234-1234.
  ```

### destroy:
  Deletes an instance based on the class name and id (save the change into the JSON file). 
  Ex:
  ```
  $ destroy BaseModel 1234-1234-1234.
  ```

### all:
  Prints all string representation of all instances based or not on the class name. 
  Example to show all instances
  ```
  $ all
  ```

  Example to show all instances of BaseModel only
  ```
  $ all BaseModel
  ```

### update:
  Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). 
  Ex: 
  ```
  $ update BaseModel 1234-1234-1234 email "airbnb@alxholbertonschool.com"
  ```

### quit:
  Quit the shell 


## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Programming language

## ✍️ Authors <a name = "authors"></a>

- [@pelumiolawole](https://github.com/pelumiolawole) - Pelumi Olawole
- [@Zandarh](https://github.com/Zandarh) - Alexander Ubaka
