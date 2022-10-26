from . import db


class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.Text, nullable=False)
    discord_contact = db.Column(db.Text, nullable=False)
    battlenet_contact = db.Column(db.Text, nullable=False)
    armory_link = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    wow_class = db.Column(db.Text, nullable=False)
    team_choice = db.Column(db.Text, nullable=False)
    primary_spec = db.Column(db.Text, nullable=False)
    raiderio_link = db.Column(db.Text, nullable=False)
    warcraftlogs_link = db.Column(db.Text, nullable=False)
    real_life_summary = db.Column(db.Text, nullable=False)
    skills_summary = db.Column(db.Text, nullable=False)
    proclivity_summary = db.Column(db.Text, nullable=False)
    pizza_question = db.Column(db.Text, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
