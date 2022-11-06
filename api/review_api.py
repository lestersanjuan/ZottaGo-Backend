import os
import sys
import json
import uuid
from flask import request

from app import app,db
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

def review_get():
    data = request.get_json()
    review = (db.session.query(Review)).filter_by(review_id=data['review_id'])
    return json.dumps({
        review_id : str(Review.review_id),
        rating : int(Review.rating),
        description : str(Review.description),
        bathroom_id : str(Review.bathroom_id)
    })

def review_set():
    data = request.get_json()
    review = (db.session.query(Review)).filter_by(review_id=data['review_id'])
    return json.dumps({
        review_id : str(uuid.uuid4()),
        rating : int(data["rating"]),
        description : str(data["description"]),
        bathroom_id : str(data["bathroom_id"])
    })