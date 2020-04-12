# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Reference
Getting Started

    Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://127.0.0.1:5000/, which is set as a proxy in the frontend configuration.
    Authentication: This version of the application does not require authentication or API keys.

Error Handling

Errors are returned as JSON objects in the following format:

{
    "success": False,
    "error": 400,
    "message": "bad request"
}

The API will return three error types when requests fail:

    404: Resource Not Found
    422: Not Processable

Endpoints
Get /questions
        General:
            Returns a list of questions depending on the category specified and the page number
        Sample:
            curl http://127.0.0.1:5000/questions?category=Art&page=1
        Response:
            {
            "categories": {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            },
            "current_category": "Art",
            "questions": [
                {
                "answer": "answer14",
                "category": "Art",
                "difficulty": 3,
                "id": 14,
                "question": "Questions14"
                },
                {
                "answer": "answer12",
                "category": "Art",
                "difficulty": 2,
                "id": 12,
                "question": "Questions12"
                },
                {
                "answer": "answer17",
                "category": "Art",
                "difficulty": 5,
                "id": 17,
                "question": "Questions17"
                },
                {
                "answer": "Answer New",
                "category": "Art",
                "difficulty": 5,
                "id": 20,
                "question": "Question"
                },
                {
                "answer": "Maya2",
                "category": "Art",
                "difficulty": 3,
                "id": 23,
                "question": "hassan1"
                }
            ],
            "success": true,
            "total_questions": 5
            }

Post /questions
        General:
            Add a new Question
        Request Body:
            type: application/json
            body sample :
                {
                    "answer": "answer14",
                    "category": "Art",
                    "difficulty": 3,
                    "question": "Questions14"
                }
        Response:
                {
                "success": true
                }

Post /questions   (Search)
        General:
            Search for questions depending on the search query in the request body
        Request Body:
            type: application/json
            body sample:
            {"searchTerm":"a"}
        Response:
            {
            "questions": [
                {
                "answer": "Maya2",
                "category": "Art",
                "difficulty": 3,
                "id": 23,
                "question": "hassan1"
                },
                {
                "answer": "Mariam",
                "category": "1",
                "difficulty": 4,
                "id": 24,
                "question": "Hamzah"
                }
            ],
            "success": true,
            "total_questions": 2
            }

Delete /questions/<question_id>
        General:
            Delete the specified question
        Sample:
            curl -X DELETE http://127.0.0.1:5000/questions/1
        Response:
                {
                "success": true
                }



Get /categories
        General:
            Getting all the categoris
        Sample:
            curl http://127.0.0.1:5000/categories
        Response:
            {
            "categories": {
                "1": "Science",
                "2": "Art",
                "3": "Geography",
                "4": "History",
                "5": "Entertainment",
                "6": "Sports"
            }
}

Get /categories/<int:cat_id>/questions
        General:
            Get questions for specified category
        Sample:
            curl http://127.0.0.1:5000/categories/1/questions
        Response:
            {
            "questions": [
                {
                "answer": "answer9",
                "category": "Science",
                "difficulty": 5,
                "id": 9,
                "question": "Questions9"
                },
                {
                "answer": "answer1",
                "category": "Science",
                "difficulty": 3,
                "id": 1,
                "question": "Questions1"
                },
                {
                "answer": "answer2",
                "category": "Science",
                "difficulty": 3,
                "id": 2,
                "question": "Questions2"
                },
                {
                "answer": "answer11",
                "category": "Science",
                "difficulty": 3,
                "id": 11,
                "question": "Questions11"
                }
            ],
            "success": true,
            "total_questions": 4
            }
