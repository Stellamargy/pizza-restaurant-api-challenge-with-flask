from server.app import db
from sqlalchemy.orm import validates  
from datetime import datetime,timezone
from sqlalchemy_serializer import SerializerMixin
class RestaurantPizza(db.Model,SerializerMixin):
    #tablename
    __tablename__="restaurantpizzas"
    #table columns
    id=db.Column(db.Integer,primary_key=True)
    prize=db.Column(db.Integer,nullable=False)
    #relationship at database level
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurants.id', ondelete='CASCADE'),nullable=False)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id', ondelete='CASCADE'),nullable=False)
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    #Relationship at model level
    restaurant=db.relationship(('Restaurant'),back_populates="restaurant_pizzas")
    pizza=db.relationship(('Pizza'),back_populates="restaurant_pizzas")
    
    #Serialization Rules -Prevent Recursion
    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas')
    #Checks for price
    @validates('prize')
    def validate_prize(self, key, value):
        if not isinstance(value, int):
            raise ValueError("Price must be an integer.")
        if value < 1 or value > 10:
            raise ValueError("Price must be between 1 and 10.")
        return value
    
    #Improve RestaurantPizza instance Readability
    def __repr__(self):
        return f"""ID:{self.id},PRIZE:{self.prize},RESTAURANT_ID:{self.restaurant_id},PIZZA_ID:{self.pizza_id},CREATED_AT:{self.created_at}"""
    