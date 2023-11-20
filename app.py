import os

from flask import Flask
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
Base = declarative_base()
engine = create_engine(os.getenv("SQLALCHEMY_URL"))


class Coach(Base):
    __tablename__ = "coach"
    coach_id = Column(Integer, primary_key=True, autoincrement=True)
    coach_email = Column(String)
    coach_password = Column(String)


class Team(Base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True, autoincrement=True)
    team_name = Column(String)
    team_number = Column(String)
    team_program = Column(String)
    coach_id = Column(Integer, ForeignKey("coach.coach_id"))


class FormEntry(Base):
    __tablename__ = "form_entry"
    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    entry_name = Column(String)
    entry_pdf_url = Column(String)
    entry_email = Column(String)


class FormToTeam(Base):
    __tablename__ = "form_to_team"
    assoc_id = Column(Integer, primary_key=True, autoincrement=True)
    entry_id = Column(Integer, ForeignKey("form_entry.entry_id"))
    team_id = Column(Integer, ForeignKey("team.team_id"))


Base.metadata.create_all(engine)


@app.route('/')
def home_page():
    return 'Would you like to <a href="/roster">load a roster</a> or <a href="/upload">upload a signed form</a>?'


@app.route('/upload', methods=["GET", "POST"])
def upload():
    return "Upload page not implemented yet"


@app.route('/roster')
def roster():
    return "Roster page not implemented yet"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
