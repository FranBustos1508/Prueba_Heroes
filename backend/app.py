from flask import Flask, request
from flask_cors import CORS
from db.characters import get_all_characters, get_character_by_id, remove_character, add_character, edit_character
from time import sleep

app = Flask(__name__)
CORS(app)

@app.route("/characters")
def all_characters():
    return get_all_characters()

@app.route("/characters/<id>")
def character_by_id(id):
    sleep(2)
    return get_character_by_id(id)

@app.route("/characters/<id>", methods = ["DELETE"])
def remove_character_by_id(id):
    return {"success": remove_character(id)}

@app.route("/characters", methods = ["POST"])
def create_character():
    name = request.json.get("name")
    names = request.json.get("names")
    publisher = request.json.get("publisher")
    gender = request.json.get("gender")
    alignment = request.json.get("alignment")
    image = request.json.get("image")
    race = request.json.get("race")

    id = int(get_all_characters()[-1]["id"]) + 1

    character = {
        "id": id,
        "name": name,
        "names": names,
        "publisher": publisher,
        "gender": gender,
        "alignment": alignment,
        "image": image,
        "race": race
    }
    return {"success": add_character(character), "id": id}

@app.route("/characters", methods = ["PUT"])
def edit_character_by_id():
    name = request.json.get("name")
    names = request.json.get("names")
    publisher = request.json.get("publisher")
    gender = request.json.get("gender")
    alignment = request.json.get("alignment")
    image = request.json.get("image")
    race = request.json.get("race")
    id = request.json.get("id")

    character = get_character_by_id(id)

    if character:
        character["name"] = name
        character["names"] = names
        character["publisher"] = publisher
        character["gender"] = gender
        character["alignment"] = alignment
        character["image"] = image
        character["race"] = race

        return {"success": edit_character(character), "id": id}
    
    return {"error": "Character not found"}, 404
    
