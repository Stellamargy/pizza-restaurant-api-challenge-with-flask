from server.app import db
from datetime import datetime,timezone
from sqlalchemy_serializer import SerializerMixin

class Restaurant(db.Model,SerializerMixin):
    #table name
    __tablename__="restaurants"
    #table columns 
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    address=db.Column(db.String(50),nullable=False)
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

    #Define Relationships -Pythonic acess/model navigation
    restaurant_pizzas=db.relationship("RestaurantPizza",back_populates="restaurant")

    #Serialization rules -remove recursion
    serialize_rules = ('-restaurant_pizzas.restaurant',)

    #Improve readability of restaurant Instances .
    def __repr__(self):
        return f"""
                ID:{self.id},NAME:{self.name},ADDRESS:{self.address},CREATED_AT:{self.created_at}
                """