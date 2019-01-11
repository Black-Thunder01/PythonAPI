# Import all the libraries, you're going to use.

from flask import Flask, request
from flask_restful import Resource, Api
from aqlalchemy import create_engine
from json import dumps
from flas.ext.jsonpify import jsonify 

# connect to the database
db_conn = create_engine('sqlite:///chinook.db');
# Create Flask app
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
	"""docstring for Employees"""
	def get(self):
		conn = db_conn.connect() # Connect to the database.
		query = conn.execute("select * from Employees") # This line performs query and returns json result
		return {'Employees': [i[0] for i in query.cursor.fetchall()]} #  Fetches first column that is Employee ID

class Track(Resource):
			"""docstring for Track"""
			def get(self):
				