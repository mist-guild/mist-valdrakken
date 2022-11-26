import os
import json
from models.applicant import Applicant
from flask import redirect, request, Blueprint
from sqlalchemy.sql import or_
from utility.webhook_utility import send_applicant_webhook

applicant = Blueprint('applicant', __name__,
                      url_prefix='/applicant', template_folder='templates')


@applicant.route('/', methods=['POST'])
def register_applicant():
    new_applicant = Applicant(character_name=request.form["character_name"],
                              discord_contact=request.form["discord_contact"],
                              battlenet_contact=request.form["battlenet_contact"],
                              armory_link=request.form["armory_link"],
                              age=request.form["age"],
                              wow_class=request.form["wow_class"],
                              team_choice=request.form["team_choice"],
                              primary_spec=request.form["primary_spec"],
                              raiderio_link=request.form["raiderio_link"],
                              warcraftlogs_link=request.form["warcraftlogs_link"],
                              real_life_summary=request.form["real_life_summary"],
                              skills_summary=request.form["skills_summary"],
                              proclivity_summary=request.form["proclivity_summary"],
                              pizza_question=request.form["pizza_question"],
                              archived_comments=None)
    new_applicant.save()
    send_applicant_webhook(new_applicant)
    website_url = os.getenv("GUILD_WEBSITE_URL")
    return redirect(website_url), 201


@applicant.route("/all", methods=["GET"])
def get_applicants():
    applicants = Applicant.query.all()
    data = {}
    for applicant in applicants:
        data[applicant.id] = applicant.character_name
    return json.dumps(data), 200


@applicant.route('/<int:applicant_id>', methods=['GET'])
def get_applicant(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    return applicant.to_json(), 200


@applicant.route('/exists', methods=['GET'])
def applicant_exists():
    # TODO: wrap a lot of logic away
    discord_contact = request.json["discord_contact"]
    battlenet_contact = request.json["battlenet_contact"]

    discord_contact = Applicant.query.filter_by(
        discord_contact=discord_contact).all()
    battlenet_contact = Applicant.query.filter_by(
        battlenet_contact=battlenet_contact).all()

    found_applicants = []
    if "called_from" in request.json:
        called_from = request.json["called_from"]
        found_applicants = [applicant.id for applicant in discord_contact +
                            battlenet_contact if applicant.id != called_from]
    else:
        found_applicants = [
            applicant.id for applicant in discord_contact + battlenet_contact]

    return [*set(found_applicants)], 200


@applicant.route('/archive/<int:applicant_id>', methods=['PUT'])
def archive_applicant(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    applicant.archived_comments = str(request.data, encoding='utf-8')
    applicant.save()
    return applicant.to_json(), 200
