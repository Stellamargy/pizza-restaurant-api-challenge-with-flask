from flask import Blueprint,jsonify,make_response

restaurant_bp=Blueprint('restaurants',__name__)
#Customized function to send Response-Keep code DRY
def api_response(message, data=None, status="success", status_code=200):
    body = {
        "status": status,
        "message": message,
        "data": data or []
    }
    return make_response(jsonify(body), status_code)

#Get all restaurants
@restaurant_bp.route('/')
def get_restaurants():
    restaurants=Restaurant.query.all()
    if restaurants:
        return api_response("Restaurant Retrieved Sucessfully",[restaurant.to_dict() for restaurant in restaurants])
    else:
        return api_response("No restaurants found.", [], status="error", status_code=404)
    

from server.app import db
from server.models.restaurant import Restaurant
