from server.app import db
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime,timezone
from sqlalchemy_serializer import SerializerMixin
class Pizza(db.Model,SerializerMixin):
    #table name
    __tablename__="pizzas"
    #Table Columns 
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    ingredients=db.Column(ARRAY(db.Text),nullable=False)
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

    #Define Relationships at model level
    restaurant_pizzas=db.relationship("RestaurantPizza",back_populates="pizza")
    #Serialization rules
    serialize_rules=('- restaurant_pizzas.pizza',)

    def __repr__(self):
        return f"""
        ID:{self.id}, NAME:{self.name}, INGREDIENTS:{self.ingredients},CREATED_AT:{self.  created_at}
                """
