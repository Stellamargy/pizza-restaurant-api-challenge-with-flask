from flask import Blueprint
from server.app import db
restaurant_bp=Blueprint('restaurants',__name__)

#Get all restaurants
@restaurant_bp.route('/')
def get_restaurants():
    restaurant=
