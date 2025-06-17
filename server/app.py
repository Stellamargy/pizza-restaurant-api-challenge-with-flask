from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from routes.restaurant_controller import restaurant_bp

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy()
migrate=Migrate()
db.init_app(app)
migrate.init_app(db=db,app=app)

#Register Blueprints
app.register_blueprint(restaurant_bp,url_prefix='/restaurants')

#Prevents circular imports 
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza




