import os
import json
from models.reagent_count import ReagentCount
from flask import redirect, request, Blueprint

reagent = Blueprint('reagent', __name__,
                       url_prefix='/reagent', template_folder='templates')


@reagent.route('/', methods=['POST'])
def register_reagent():
    new_reagent = ReagentCount(character_name=request.form["character_name"],
                                 hochenblume_bronze=0,
                                 writhebark_gold=0,
                                 bubble_poppy_bronze=0,
                                 bubble_poppy_silver=0)
    new_reagent.save()
    return "Reagent successfully created!", 201


@reagent.route('/<string:character_name>', methods=['GET', 'PUT'])
def get_put_by_character_name(character_name):
    if request.method == 'GET':
        reagent = ReagentCount.query.filter_by(
            character_name=character_name).first()
        return reagent.to_json(), 200
    elif request.method == 'PUT':
        print(request.json)
        print("based")
        return 200
