import os
import sys
import json
import uuid
from flask import request

from app import app,db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from componenets.bathroom.Bathrooms import Bathrooms


#@app.route
def bathroom_get():
    data = request.get_json()
    bathroom = (db.session.query(Bathroom)).filter_by(bathroom_id=data['bathroom_id']).first()
    return json.dumps({
        bathroom_ID: str(Bathrooms.bathroom_id),
        name_of_building: str(Bathrooms.name_of_building),
        floor_number: int(Bathrooms.floor_number)
        directions: str(Bathrooms.direction)
    })

def bathroom_set():
    data = request.get_json()
    bathroom = (db.session.query(Bathroom)).filter_by(bathroom_id=data['bathroom_id']).first()
    addBathroom = Bathroom(
        bathroom_id : str(uuid.uuid4()),
        name_of_building : str(data["name_of_building"])
        floor_number : int(data["review_id"])
        direction : str(data["direction"]) 
    )

