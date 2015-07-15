from routes import db
from models import Quiz

#create the database and the db tables
db.create_all()

# insert
db.session.add(Quiz("Which of the options best describes a goat?", "animal", "plant", "animal"))
db.session.add(Quiz("Which of the options is true?", "A goat is an animal", "plant is an animal", "animal"))


# commit the changes
db.session.commit()