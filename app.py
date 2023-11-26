import os

import flask
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

if not os.path.exists("uploads"):
    os.mkdir("uploads")


@app.route('/')
def home_page():
    return ('<h1>Welcome to CandR</h1><br>Would you like to <a href="/roster">load a roster</a> or '
            '<a href="/upload">upload a signed form</a>?')


@app.route('/upload', methods=["GET", "POST"])
def upload():
    if flask.request.method == "GET":
        return flask.send_from_directory("static", "upload.html")
    else:
        form_data = flask.request.form
        print(type(form_data['fileup']), flush=True)  # huh...where did the file data go?
        print(form_data, flush=True)
        teams = []
        name = form_data.get("name")
        for key in form_data.keys():
            if key.startswith("teamno"):
                team_no = form_data.get(key)
                team_type = form_data.get("teamtype" + str(key[6:]))
                teams.append({team_no: team_type})
        print("Name and teams", name, teams, flush=True)
        # Verify if entered teams exist in database, return error if not
        # Insert entry record into database
        # Insert teamassoc records into database
        return "Your form was successfully uploaded. You may <a href=\"/upload\">upload more.</a>"


@app.route('/roster')
def roster():
    # TODO implement entire page
    # Once logged in, SELECT team_id FROM team where coach_id = logged in user
    # Then return a table of *FormEntry* names where team_id in those IDs.
    return "Roster page not implemented yet"


@app.route("/upload.js")
def upload_js():
    return flask.send_from_directory("static", "upload.js")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
