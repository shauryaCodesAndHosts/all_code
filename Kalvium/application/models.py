from .database import db 

class History(db.Model):
    __tablename__ = 'history'
    historyId = db.Column(db.Integer, autoincrement = True , primary_key = True , nullable = False)
    mathString = db.Column(db.String, nullable = False)
    timeOfEntry = db.Column(db.String)
    def serialize(self):
        return {
            "Question" : self.mathString,
            "Answer" : eval(self.mathString)
        }