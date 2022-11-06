import os
import sys
import json
import uuid
from flask import request

from app import app,db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


from components.floor.Floor import Floor

def floor_get():
    data = request.get_json()
    floor = (db.session.query(Floor)).filter_by(floor_id=floor_data["floor_id"]).first()
    return json.dumps({ 
        floor_id : str(Floor.floor_id),
        bathroom_id : str(Floor.bathroom_id),
        floor_number : int(Floor.floor_number),
        name_of_building : str(Floor.name_of_building),
    })

def floor_set():
    data = request.get_json()
    floor = (db.session.query(Floor)).filter_by(floor_id=floor_data["floor_id"]).first()
    return json.dumps({
        floor_id : str(uuid.uuid4()),
        bathroom_id : str(data["bathroom_id"]),
        floor_number : int(data["floor_number"]),
        name_of_building : str(data["name_of_building"])
    })