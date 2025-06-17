from flask import Blueprint,jsonify,make_response
# Restaurant Blueprint
restaurant_bp=Blueprint('restaurants',__name__)
#Customized function to create Responses-Keep code DRY
def api_response(message, data=None, status="success", status_code=200):
    body = {
        "status": status,
        "message": message,
        "data": data 
    }
    return make_response(jsonify(body), status_code)

#Get all restaurants
@restaurant_bp.route('/')
def get_restaurants():
    restaurants=Restaurant.query.all()
    if restaurants:
        return api_response(message="Restaurants Retrieved Sucessfully",data=[restaurant.to_dict_basic() for restaurant in restaurants])
    else:
        return api_response(message="No Restaurants Data", data=restaurants.to_dict_basic())
    
#Delete a restaurant by id
@restaurant_bp.route('/<int:id>')
def get_restaurant(id):
    restaurant=Restaurant.query.get(id)
    if restaurant:     
        return api_response("Restaurant Retrieved Successfully",restaurant.to_dict_basic())
    else:
        return api_response(f"No Restaurant with id:{id}",status="Error",status_code=404)
    
#Delete restaurant by id
@restaurant_bp.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204  
    else:
        return api_response(f"Cannot delete. No Restaurant with id: {id}", status="error", status_code=404)

    
    

from server.app import db
from server.models.restaurant import Restaurant
