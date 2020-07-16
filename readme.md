# Simple Todo List API
## Requirements
This project require the following dependencies:

- python 3.8.x
- [pipenv](https://pypi.org/project/pipenv/)

## Get Started
```shell script
# Create a folder for the project
$ mkdir todo_list & cd todo_list
# Clone the Github repo
$ git clone git@github.com:minhvu-tbg/todo_list.git .
# Activate virtual environment
$ pipenv shell
# Install packages (only need to do this once)
$ pipenv install
```

## Deployment
Run the server with:
```shell script
$ uvicorn app:app --reload
```

Open your browser at http://127.0.0.1:8000/users/.

### Interactive API docs
View documentations via  http://127.0.0.1:8000/docs.