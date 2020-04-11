import os
from flask import Flask, request, abort, jsonify ,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TOTO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app , resources={r"/*":{"origins":"*"}})

  '''
  @TOTO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
        response.headers.add("Access-Control-Allow-Headers","Content-Type,Authorization")
        response.headers.add("Access-Control-Allow-Methods","GET,POST,PATCH,DELETE")
        return response 
  
  '''
  @TOTO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories',methods=['GET'])
  def get_all_categories():
       allCats = {} 
       try:
            for cat in Category.query.all():
                  allCats[cat.id] = cat.type
            
            if len (allCats) == 0:
                  abort(404)
            return jsonify({
                  'categories':allCats
            })
       except:
             abort(404)


  '''
  @TOTO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions',methods=['GET'])
  def get_questions():
      page = int(request.args.get('page','1'))
      try:
            start = (page-1)*QUESTIONS_PER_PAGE
            end = start + QUESTIONS_PER_PAGE
            category = request.args.get('category',None)
            allCats = {} 
            for cat in Category.query.all():
                  allCats[cat.id] = cat.type
            
            #formattedCats = [cat.format() for cat in allCats]
            if category == None:
                  allQuestions = Question.query.all()
                  allQuestions_formatted = [question.format() for question in allQuestions]
                  return jsonify({
                        'success':True , 
                        'total_questions':len(allQuestions) , 
                        'questions':allQuestions_formatted[start:end],
                        'current_category':'None' , 
                        'categories':allCats
                        
                  })
            else:
                  allQuestions = Question.query.filter(Question.category == category).all()
                  allQuestions_formatted = [question.format() for question in allQuestions]
                  return jsonify({
                        'success':True , 
                        'total_questions':len(allQuestions) , 
                        'questions':allQuestions_formatted[start:end],
                        'current_category':category , 
                        'categories':allCats
                        
                  })
      except:
            abort (404)

  '''
  @TOTO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST ✅: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>' , methods=['DELETE'])
  def delete_question(question_id):
        question = Question.query.get(question_id)
        question.delete()
        return jsonify({"success":True})
  '''
  @TOTO:✅ 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST 👍🏻: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  
  '''
  @TOTO✅: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST👍🏻: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions',methods=['POST'])
  def add_new_question():
        try:
            body = request.get_json()
            search = body.get('searchTerm' , None)
            if search == None:  
                  ques = body.get('question')
                  answer = body.get('answer')
                  category = body.get('category')
                  difficulty = body.get('difficulty')
                  question = Question(ques , answer , category , difficulty)
                  question.insert()
                  return jsonify({
                        "success":True
                  })
            else : 
                  allQuestions = Question.search(search)
                  return jsonify({
                        'success':True , 
                        'total_questions':len(allQuestions) , 
                        'questions':allQuestions,
                  
                  })  
        except:
              abort(422)


  '''
  @TOTO✅: 
  Create a GET endpoint to get questions based on category. 

  TEST👍🏻: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/questions/<category_name>')
  def get_questions_by_category(category_name):
        try:
              
            allQuestions = Question.searchByCaegories(category_name)
            return jsonify({
                  "success":True , 
                  "questions":allQuestions , 
                  'total_questions':len(allQuestions) 
            })
        except:
              abort(404)

  @app.route('/categories/<int:cat_id>/questions')
  def get_questions_by_cat_id(cat_id):
      try:
        category = Category.query.get(cat_id)
        allQuestions = Question.searchByCaegories(category.type)
        return jsonify({
              "success":True , 
              "questions":allQuestions , 
              'total_questions':len(allQuestions) 
        })
      except:
        abort(404)

  '''
  @TOTO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def get_random_question():
        
        body = request.get_json()
        category = body.get('quizCategory' , None)
        allQuestions = Question.GetRandomQuestion(category)
        return jsonify({
              "success":True , 
              "total_questions": len(allQuestions), 
              "question":allQuestions
            
        })



  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found():
        return jsonify({
              "success":False ,
              "error":404 , 
              "message":"Can not find the page"
        }) , 404
            
  @app.errorhandler(422)
  def notrecognized():
        return jsonify({
              "success":False ,
              "error":422 , 
              "message":"Can not handle request"
              
              }),422 
      
  return app

    