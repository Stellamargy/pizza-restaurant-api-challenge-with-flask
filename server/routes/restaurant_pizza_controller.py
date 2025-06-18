from flask import Blueprint,make_response,jsonify,request
#create restaurant_pizza blueprint
restaurantpizza_bp=Blueprint("restaurantpizzas",__name__)

#Post Restaurant Pizza
@restaurantpizza_bp.route("/",method=['POST'])
def create_restaurantpizza():
    pass