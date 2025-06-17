from flask import Blueprint,make_response,jsonify
#Pizza Blueprint
pizza_bp=Blueprint("pizzas",__name__)

#Customized function to create Responses-Keep code DRY
def api_response(message, data=None, status="success", status_code=200):
    body = {
        "status": status,
        "message": message,
        "data": data 
    }
    return make_response(jsonify(body), status_code)

#Get all pizzas
@pizza_bp.route('/')
def get_pizzas():
    pizzas=Pizza.query.all()
    if pizzas:
        return api_response(message="Pizzas retrieved successfully", data=[pizza.to_dict_basic() for pizza in pizzas], status="success", status_code=200)
    else:
        return api_response(message="No Pizza Data", data=pizzas.to_dict_basic())



from server.app import db
from server.models.pizza import Pizza