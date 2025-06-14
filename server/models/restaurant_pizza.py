from server.app import db
from datetime import datetime,timezone

class RestaurantPizza(db.Model):
    #tablename
    __tablename__="restaurantpizzas"
    #table columns
    id=db.Column(db.Integer,primary_key=True)
    prize=db.Column(db.Integer,nullable=False)
    #relationship at database level
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurants.id'),nullable=False)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id'),nullable=False)
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
    restaurant=db.relationship(('Restaurant'),back_populates="restaurant_pizza")
    pizza=db.relationship(('Pizza'),back_populates="restaurant_pizza")
    
    #Improve RestaurantPizza instance Readability
    def __repr__(self):
        return f"""ID:{self.id},PRIZE:{self.prize},RESTAURANT_ID:{self.restaurant_id},PIZZA_ID:{self.pizza_id},CREATED_AT:{self.created_at}"""