from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy()
migrate=Migrate()
db.init_app(app)
migrate.init_app(db=db,app=app)

#Prevents circular imports 
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza




