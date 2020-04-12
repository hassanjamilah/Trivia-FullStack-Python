import os
from sqlalchemy import Column, String, Integer, create_engine , Boolean
from flask_sqlalchemy import SQLAlchemy
import json
import random

database_name = "trivia"
database_path = "postgres://{}@{}/{}".format('postgres','localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Question

'''
class Question(db.Model):  
  __tablename__ = 'questions'

  id = Column(Integer, primary_key=True)
  question = Column(String)
  answer = Column(String)
  category = Column(String)
  difficulty = Column(Integer)
  

  def __init__(self, question, answer, category, difficulty):
    self.question = question
    self.answer = answer
    self.category = category
    self.difficulty = difficulty
    

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()


  def GetRandomQuestion(category , prevQuestions):
        allQuestions = [] 
        allQuestions1 = []
        if category == None:
              allQuestions = db.session.query(Question.id).all()
        else:
              allQuestions = db.session.query(Question.id).filter(Question.category == category).all()
        print (prevQuestions)
        for question in allQuestions:
            if  not question[0] in prevQuestions:
                 allQuestions1.append(question)
        num = random.randrange(0, len(allQuestions1) , 1) 
        questId = allQuestions1[num]
        question = Question.query.get(questId)
        return question.format()        

  def search( search_term):
        questions = Question.query.filter(Question.question.ilike("%{}%".format(search_term)) ).all()
        formatted_questions = [question.format() for question in questions]
        return formatted_questions
  def searchByCaegories(categoryName):
        questions = Question.query.filter(Question.category.ilike("%{}%".format(categoryName))).all()
        formatted_questions = [question.format() for question in questions]
        return formatted_questions
        
  def format(self):
    return {
      'id': self.id,
      'question': self.question,
      'answer': self.answer,
      'category': self.category , 
      'difficulty': self.difficulty
    }

'''
Category

'''
class Category(db.Model):  
  __tablename__ = 'categories'

  id = Column(Integer, primary_key=True)
  type = Column(String)

  def __init__(self, type):
    self.type = type

  def format(self):
    return {
      'id': self.id,
      'type': self.type
    }