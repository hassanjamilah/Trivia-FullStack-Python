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

Post /questions   (Search)


Delete /questions/<question_id>



Get /categories

Get /categories/<int:cat_id>/questions

GET /books

    General:
        Returns a list of book objects, success value, and total number of books
        Results are paginated in groups of 8. Include a request argument to choose page number, starting from 1.
    Sample: curl http://127.0.0.1:5000/books

  "books": [
    {
      "author": "Stephen King",
      "id": 1,
      "rating": 5,
      "title": "The Outsider: A Novel"
    },
    {
      "author": "Lisa Halliday",
      "id": 2,
      "rating": 5,
      "title": "Asymmetry: A Novel"
    },
    {
      "author": "Kristin Hannah",
      "id": 3,
      "rating": 5,
      "title": "The Great Alone"
    },
    {
      "author": "Tara Westover",
      "id": 4,
      "rating": 5,
      "title": "Educated: A Memoir"
    },
    {
      "author": "Jojo Moyes",
      "id": 5,
      "rating": 5,
      "title": "Still Me: A Novel"
    },
    {
      "author": "Leila Slimani",
      "id": 6,
      "rating": 5,
      "title": "Lullaby"
    },
    {
      "author": "Amitava Kumar",
      "id": 7,
      "rating": 5,
      "title": "Immigrant, Montana"
    },
    {
      "author": "Madeline Miller",
      "id": 8,
      "rating": 5,
      "title": "CIRCE"
    }
  ],
"success": true,
"total_books": 18
}

POST /books

    General:
        Creates a new book using the submitted title, author and rating. Returns the id of the created book, success value, total books, and book list based on current page number to update the frontend.
    curl http://127.0.0.1:5000/books?page=3 -X POST -H "Content-Type: application/json" -d '{"title":"Neverwhere", "author":"Neil Gaiman", "rating":"5"}'

{
  "books": [
    {
      "author": "Neil Gaiman",
      "id": 24,
      "rating": 5,
      "title": "Neverwhere"
    }
  ],
  "created": 24,
  "success": true,
  "total_books": 17
}

DELETE /books/{book_id}

    General:
        Deletes the book of the given ID if it exists. Returns the id of the deleted book, success value, total books, and book list based on current page number to update the frontend.
    curl -X DELETE http://127.0.0.1:5000/books/16?page=2

{
  "books": [
    {
      "author": "Gina Apostol",
      "id": 9,
      "rating": 5,
      "title": "Insurrecto: A Novel"
    },
    {
      "author": "Tayari Jones",
      "id": 10,
      "rating": 5,
      "title": "An American Marriage"
    },
    {
      "author": "Jordan B. Peterson",
      "id": 11,
      "rating": 5,
      "title": "12 Rules for Life: An Antidote to Chaos"
    },
    {
      "author": "Kiese Laymon",
      "id": 12,
      "rating": 1,
      "title": "Heavy: An American Memoir"
    },
    {
      "author": "Emily Giffin",
      "id": 13,
      "rating": 4,
      "title": "All We Ever Wanted"
    },
    {
      "author": "Jose Andres",
      "id": 14,
      "rating": 4,
      "title": "We Fed an Island"
    },
    {
      "author": "Rachel Kushner",
      "id": 15,
      "rating": 1,
      "title": "The Mars Room"
    }
  ],
  "deleted": 16,
  "success": true,
  "total_books": 15
}

PATCH /books/{book_id}

    General:
        If provided, updates the rating of the specified book. Returns the success value and id of the modified book.
    curl http://127.0.0.1:5000/books/15 -X PATCH -H "Content-Type: application/json" -d '{"rating":"1"}'

{
  "id": 15,
  "success": true
}
