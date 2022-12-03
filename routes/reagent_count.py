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
    reagent = ReagentCount.query.filter_by(
        character_name=character_name).first()

    if request.method == 'GET':
        if reagent is None:
            return "Reagent not found!", 404
        return reagent.to_json(), 200
    elif request.method == 'PUT':
        # if reagent is None, create reagent
        if reagent is None:
            reagent = ReagentCount(character_name=character_name)
            attrs = [attr for attr in dir(reagent)
                     if not callable(getattr(reagent, attr)) and
                     not attr.startswith("__") and
                     not attr.startswith("_")]
            for attr in attrs:
                if attr == "character_name" or attr == "id":
                    continue
                setattr(reagent, attr, 0)

        # update reagent
        del request.json['Character']
        for data in request.json:
            setattr(reagent,
                    convert_reagent_name(data),
                    request.json[data])
        reagent.save()

        # return reagent
        return "Reagent successfully saved!", 200


# TODO: move to service
def convert_reagent_name(reagent_name):
    reagent_name = reagent_name.lower()
    reagent_name = reagent_name.replace(' - ', '_')
    reagent_name = reagent_name.replace('-', '_')
    reagent_name = reagent_name.replace("'s", 's')
    reagent_name = reagent_name.replace(' ', '_')
    return reagent_name
