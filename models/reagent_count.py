from . import db


class ReagentCount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.Text, nullable=False)
    hochenblume_bronze = db.Column(db.Integer, nullable=False)
    writhebark_gold = db.Column(db.Integer, nullable=False)
    bubble_poppy_bronze = db.Column(db.Integer, nullable=False)
    bubble_poppy_silver = db.Column(db.Integer, nullable=False)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __str__(self) -> str:
        return self.character_name + ": " + self.id
    
    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
