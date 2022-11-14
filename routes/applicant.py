import os
import json
import base64
import zlib
from models.applicant import Applicant
from flask import redirect, request, Blueprint
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


@applicant.route('/<int:applicant_id>', methods=['GET'])
def get_applicant(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    return applicant.to_json(), 200


@applicant.route('/archive/<int:applicant_id>', methods=['PUT'])
def archive_applicant(applicant_id):
    applicant = Applicant.query.filter_by(id=applicant_id).first()
    applicant.archived_comments = str(request.data, encoding='utf-8')
    applicant.save()
    return applicant.to_json(), 200


@applicant.route('/a')
def a():
    applicant = Applicant.query.filter_by(id=20).first()
    a = zlib.decompress(base64.b64decode(
        bytes(applicant.archived_comments, encoding='utf-8')
    )).decode()
    return a, 200
