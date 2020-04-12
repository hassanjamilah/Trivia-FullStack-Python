import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TOTO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        
        self.assertTrue(data['categories'])
        self.assertEqual(len(data['categories']),6)
     
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
    
        self.assertEqual(data['success'] , True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertGreater(data['total_questions'] , 0)
     
    
    def test_get_questions_with_category(self):
        res = self.client().get('/questions?category=Art')
        data = json.loads(res.data)    
        
        
        self.assertEqual(data['success'] , True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['categories'])
        self.assertGreater(data['total_questions'] , 0)
        
    def test_delete_question(self):
        res = self.client().delete('/questions/1')
        data = json.loads(res.data)
        
        self.assertEqual(data['success'],True)
        
        
    def test_add_new_question(self):
        res = self.client().post('/questions' , json={
                                        "answer": "Answer New1",
                                        "category": "Art",
                                        "difficulty": 5,
                                        "id": 20,
                                        "question": "Question23"
                                        })
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
        
    def test_search_question_by_post(self):
        res = self.client().post('/questions' , json={'searchTerm','a'})
        data = json.loads(res.data)
        
        self.assertEqual(data['success'],True)
        self.assertTrue(data['questions'])
     
        
    def get_questions_by_category(self):
        res = self.client().get('/questions/Art')
        data = json.loads(res.data)
        
        self.assertTrue(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        
    def test_get_questions_by_cat_id(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        
        self.assertTrue(data['success'],True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['questions'])
        
    def test_get_random_question(self):
        res = self.client().post('/quizzes' , json={"quizCategory":[2,5] })
        data = json.loads(res.data)
        
        question = data['question']
        self.assertNotEqual(question.id , 2)
        self.assertNotEqual(question.id , 5)
        self.assertTrue(data['question'])
        self.assertEqual(data['success'] , True)
        
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()