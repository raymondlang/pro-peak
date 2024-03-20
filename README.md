

## Disclaimer
* This is for educational purposes only, and the code is not production-ready.

## Intro
* I created a project that uses FastAPI and follows the hexagonal architecture rules. This project is a simplified gym management software. We have functionalities like:

## Gym Clients
* Create a gym client
* Change client's personal data
* Archive a client
* Export all clients as a CSV or JSON file to S3 or Dropbox storage

## Gym Passes
* Create a gym pass
* Pause a gym pass
* Renew a gym pass
* Check if gym pass is active

## Gym Classes (CRUD)
* Create a gym class
* Delete a gym class
* Modify a gym class
* List all gym classes sorted by time and day of the week

# Project Structure
![propeak-api](https://github.com/raymondlang/pro-peak/assets/16345938/8476d9f0-6802-49b5-a4a5-109389f946c0)

## Stack
* Python 3.10
* FastAPI
* MongoDB

## Prerequisites
* Make sure you have installed all the following prerequisites on your development machine:
  * Python 3.9
  * Poetry
  * GIT
  * Make
  * Docker version >= 20.10.7
  * docker-compose version >= 1.29.2

## Setup
1. Install dependencies:
```
$ poetry install
```
2. Setup pre-commit hooks before committing:
```
$ poetry run pre-commit install
```

## Running app locally
In the main project's directory create a new ```.env``` file and copy all variables from ```example.env``` there.
Run ```docker-compose up -d```
Go to ```src/app.py``` and run the app

## Running tests

```
$ poetry run pytest
```
or 

```
$ make tests
```
