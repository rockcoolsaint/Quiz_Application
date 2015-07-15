from routes import db

class Quiz(db.Model):

	__tablename__ = "quest"

	id = db.Column(db.Integer, primary_key=True)
	question = db.Column(db.String, nullable=False)
	option_1 = db.Column(db.Integer, nullable=False)
	option_2 = db.Column(db.Integer, nullable=False)
	ans = db.Column(db.Integer, nullable=False)

	def __init__(self, question, option_1, option_2, ans):
		self.question = question
		self.option_1 = option_1
		self.option_2 = option_2
		self.ans = ans

	def __repr__(self):
		return '<name{}'.format(self.question, self.option_1, self.option_2)