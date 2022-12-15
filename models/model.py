from .db import db
class Malename(db.Document):
    fn_id= db.IntField()
    name= db.StringField()

    def to_json(self):
        return {
            "fn_id": self.fn_id,
            "name": self.name,
        }

class Femalename(db.Document):
    fn_id= db.IntField()
    name= db.StringField()

    def to_json(self):
        return {
            "fn_id": self.fn_id,
            "name": self.name,
        }

class Lastname(db.Document):
    fn_id= db.IntField()
    name= db.StringField()

    def to_json(self):
        return {
            "fn_id": self.fn_id,
            "name": self.name,
        }

class Streetname(db.Document):
    fn_id= db.IntField()
    street= db.StringField()

    def to_json(self):
        return {
            "fn_id": self.fn_id,
            "name": self.street,
        }